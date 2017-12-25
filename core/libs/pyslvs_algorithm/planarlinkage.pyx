# -*- coding: utf-8 -*-
from libc.math cimport isnan
import tinycadlib
from tinycadlib import (
    PLAP,
    PLLP,
    PLPP,
    legal_crank,
    legal_triangle,
    Coordinate
)
import numpy as np
cimport numpy as np

cdef object formula = {
    'PLAP':PLAP,
    'PLLP':PLLP,
    'PLPP':PLPP
}

#This class used to verified kinematics of the linkage mechanism.
cdef class build_planar(object):
    cdef int POINTS, count, _tmp, VARS
    cdef object formula, ExpressionL, ExpressionNameL, constraint, Exp, Link
    cdef str Driving, Follower, targetPoint, Link_str, ExpressionName_str, Expression_str
    cdef np.ndarray target
    
    def __cinit__ (self, object mechanismParams):
        self.VARS = mechanismParams['VARS']
        #target point
        self.targetPoint = mechanismParams['Target']
        # counting how many action to satisfied require point
        self.POINTS = len(mechanismParams['targetPath'])
        # driving point, string
        self.Driving = mechanismParams['Driving']
        # folower point, string
        self.Follower = mechanismParams['Follower']
        #constraint
        self.constraint = mechanismParams['constraint']
        
        # use tuple data, create a list of coordinate object
        #[Coordinate(x0, y0), Coordinate(x1, y1), Coordinate(x2, y2), ...]
        self.target = np.ndarray((self.POINTS,), dtype=np.object)
        for i, (x, y) in enumerate(mechanismParams['targetPath']):
            self.target[i] = Coordinate(x, y)
        
        # Expression A, L0, a0, D, B, B, L1, L2, D, C, B, L3, L4, C, E
        # split Expression to list
        self.Expression_str = mechanismParams['Expression']
        ExpressionL = mechanismParams['Expression'].split(',')
        
        # Link L0, L1, L2, L3, ...
        self.Link = [L for L in ExpressionL if 'L' in L]
        
        # ExpressionName PLAP, PLLP, PLLP
        # split ExpressionName to list
        self.ExpressionName_str = mechanismParams['ExpressionName']
        ExpressionNameL = mechanismParams['ExpressionName'].split(',')
        
        # combine ExpressionName and Expression, to set Expression List
        # counter,
        # PLLP -> A,L1,L2,D,B  the B will be equation target
        # the reset will be parameter of PLLP
        count = 0
        self.Exp = []
        for ExpressN in ExpressionNameL:
            _tmp = count+len(ExpressN)
            relate = ExpressN
            params = ExpressionL[count:_tmp]
            target = ExpressionL[_tmp]
            count = _tmp + 1
            self.Exp.append({"relate":relate, 'target':target, 'params':params})
        '''
        Exp: Tuple[Dict]
        {'relate': 'PLAP', 'target': 'B', 'params': ['A', 'L0', 'a0', 'D']}
        {'relate': 'PLLP', 'target': 'C', 'params': ['B', 'L1', 'L2', 'D']}
        '''
    
    cpdef object get_path(self):
        return [(c.x, c.y) for c in self.target]
    cpdef str get_Driving(self):
        return self.Driving
    cpdef str get_Follower(self):
        return self.Follower
    cpdef str get_Target(self):
        return self.targetPoint
    cpdef object get_Link(self):
        return self.Link
    cpdef str get_ExpressionName(self):
        return self.ExpressionName_str
    cpdef str get_Expression(self):
        return self.Expression_str
    
    def __call__(self, object v):
        """
        v: a list of parameter [Ax, Ay, Dx, Dy, ...]
        target: a list of target [(1,5), (2,5), (3,5)]
        POINT: length of target
        VARS: linkage variables
        """
        cdef int i
        cdef double x, y
        #Large fitness
        cdef int FAILURE = 9487
        # all variable
        cdef object tmp_dict = dict()
        # driving
        tmp_dict[self.Driving] = Coordinate(v[0], v[1])
        # follower
        tmp_dict[self.Follower] = Coordinate(v[2], v[3])
        # links
        for i, L in enumerate(self.Link):
            tmp_dict[L] = v[4+i]
        for constraint in self.constraint:
            if not legal_crank(tmp_dict[constraint['driver']], tmp_dict[constraint['follower']], tmp_dict[constraint['connect']], tmp_dict[self.Driving].distance(tmp_dict[self.Follower])):
                return FAILURE
        # calculate the target point, and sum all error.
        cdef object path = []
        cdef double sum = 0
        for i in range(self.POINTS):
            #a0: random angle to generate target point.
            #match to path points.
            tmp_dict['a0'] = np.deg2rad(v[self.VARS+i])
            for e in self.Exp:
                #formula['PLLP'](tmp_dict['B'], tmp_dict['L1'], tmp_dict['L2'], tmp_dict['D'])
                x, y = formula[e["relate"]](*[tmp_dict[p] for p in e["params"]])
                if isnan(x) or isnan(y):
                    return FAILURE
                target_coordinate = Coordinate(x, y)
                if not legal_triangle(target_coordinate, tmp_dict[e["params"][0]], tmp_dict[e["params"][-1]]):
                    return FAILURE
                tmp_dict[e["target"]] = target_coordinate
            path.append(tmp_dict[self.targetPoint])
            sum += path[i].distance(self.target[i])
        # swap
        for i in range(self.POINTS):
            for j in range(self.POINTS):
                if path[j].distance(self.target[i])<path[i].distance(self.target[i]):
                    path[i], path[j] = path[j], path[i]
        if isnan(sum):
            return FAILURE
        return sum
    
    cpdef object get_coordinates(self, object v):
        cdef int i
        cdef double x, y
        cdef str L, P
        cdef object e
        cdef object final_dict = dict()
        # driving
        final_dict[self.Driving] = Coordinate(v[0], v[1])
        # follower
        final_dict[self.Follower] = Coordinate(v[2], v[3])
        # links
        for i, L in enumerate(self.Link):
            final_dict[L] = v[4+i]
        final_dict['a0'] = np.deg2rad(v[self.VARS])
        for e in self.Exp:
            final_dict[e["target"]] = Coordinate(*formula[e["relate"]](*[final_dict[p] for p in e["params"]]))
        return final_dict
