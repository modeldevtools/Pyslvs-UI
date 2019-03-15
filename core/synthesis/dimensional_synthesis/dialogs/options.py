# -*- coding: utf-8 -*-

"""The option dialog use to adjust the setting of algorithm."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from enum import Enum, unique
from typing import (
    List,
    Tuple,
    Dict,
    Optional,
    Any,
)
from core.QtModules import (
    Slot,
    Qt,
    QDialog,
    QTableWidgetItem,
    QDoubleSpinBox,
    QSpinBox,
    QWidget,
)
from core.info import html
from .Ui_options import Ui_Dialog


GeneticPrams = {
    'nPop': 500,
    'pCross': 0.95,
    'pMute': 0.05,
    'pWin': 0.95,
    'bDelta': 5.,
}

FireflyPrams = {
    'n': 80,
    'alpha': 0.01,
    'beta_min': 0.2,
    'gamma': 1.,
    'beta0': 1.,
}

DifferentialPrams = {
    'strategy': 1,
    'NP': 400,
    'F': 0.6,
    'CR': 0.9,
}

defaultSettings = {'max_gen': 1000, 'report': 50}


@unique
class AlgorithmType(Enum):

    """Enum type of algorithms."""

    RGA = "Real-coded Genetic Algorithm"
    Firefly = "Firefly Algorithm"
    DE = "Differential Evolution"

    def __str__(self):
        return str(self.value)


class AlgorithmOptionDialog(QDialog, Ui_Dialog):

    """Option dialog.

    Only edit the settings after closed.
    """

    def __init__(
        self,
        algorithm: AlgorithmType,
        settings: Dict[str, Any],
        parent: QWidget
    ):
        """Load the settings to user interface."""
        super(AlgorithmOptionDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle(f"{algorithm.value} Options")

        self.__algorithm = algorithm
        self.__init_alg_table()
        self.alg_table.setColumnWidth(0, 200)
        self.alg_table.setColumnWidth(1, 90)
        self.__set_args(settings)

    def __init_alg_table(self):
        """Initialize the algorithm table widgets."""

        def write_table(
            integers: Optional[List[Tuple[str, str, str]]] = None,
            floats: Optional[List[Tuple[str, str, str]]] = None
        ):
            """Use to write table data."""
            if integers is None:
                integers = []
            if floats is None:
                floats = []
            i = 0
            for options, box, max_value in (
                (integers, QSpinBox, 9),
                (floats, QDoubleSpinBox, 10.)
            ):
                for name, tooltip, tooltip in options:
                    self.alg_table.insertRow(i)
                    name_cell = QTableWidgetItem(name)
                    name_cell.setToolTip(tooltip)
                    self.alg_table.setItem(i, 0, name_cell)
                    spinbox = box()
                    spinbox.setMaximum(max_value)
                    spinbox.setToolTip(tooltip)
                    self.alg_table.setCellWidget(i, 1, spinbox)
                    i += 1

        if self.__algorithm == AlgorithmType.RGA:
            write_table(
                floats=[
                    ("Crossover Rate", 'pCross',
                        html("The chance of crossover.")),
                    ("Mutation Rate", 'pMute',
                        html("The chance of mutation.")),
                    ("Winning Rate", 'pWin',
                        html("The chance of winning.")),
                    ("Delta value", 'bDelta',
                        html("The power value when matching chromosome."))
                ]
            )
        elif self.__algorithm == AlgorithmType.Firefly:
            write_table(
                floats=[
                    ("Alpha value", 'alpha', html(
                        "Alpha value is the step size of the firefly.")),
                    ("Minimum Beta value", 'beta_min', html(
                        "The minimal attraction, must not less than this.")),
                    ("Gamma value", 'gamma', html(
                        "Beta will multiplied by exponential power value "
                        "with this weight factor.")),
                    ("Beta0 value", 'beta0', html(
                        "The attraction of two firefly in 0 distance."))
                ]
            )
        elif self.__algorithm == AlgorithmType.DE:
            write_table(
                integers=[
                    ("Evolutionary strategy (0-9)", 'strategy',
                        html("There are 10 way to evolution."))
                ],
                floats=[
                    ("Weight factor", 'F', html(
                        "Weight factor is usually between 0.5 and 1"
                        "(in rare cases > 1).")),
                    ("Recombination factor", 'CR',
                        html("The chance of crossover possible."))
                ]
            )

    def __set_args(self, settings: Dict[str, Any]):
        """Set arguments by settings dict."""
        if 'max_gen' in settings:
            self.max_gen.setValue(settings['max_gen'])
        elif 'min_fit' in settings:
            self.min_fit_option.setChecked(True)
            self.min_fit.setValue(settings['min_fit'])
        elif 'max_time' in settings:
            self.max_time_option.setChecked(True)
            # In second (int).
            max_time = settings['max_time']
            self.max_time_h.setValue(max_time // 3600)
            self.max_time_m.setValue((max_time % 3600) // 60)
            self.max_time_s.setValue(max_time % 3600 % 60)
        self.report.setValue(settings['report'])
        if self.__algorithm == AlgorithmType.RGA:
            self.pop_size.setValue(settings['nPop'])
            for i, tag in enumerate(['pCross', 'pMute', 'pWin', 'bDelta']):
                self.alg_table.cellWidget(i, 1).setValue(settings[tag])
        elif self.__algorithm == AlgorithmType.Firefly:
            self.pop_size.setValue(settings['n'])
            for i, tag in enumerate(['alpha', 'beta_min', 'gamma', 'beta0']):
                self.alg_table.cellWidget(i, 1).setValue(settings[tag])
        elif self.__algorithm == AlgorithmType.DE:
            self.pop_size.setValue(settings['NP'])
            for i, tag in enumerate(['strategy', 'F', 'CR']):
                self.alg_table.cellWidget(i, 1).setValue(settings[tag])

    @Slot(name='on_reset_button_clicked')
    def __reset(self):
        """Reset the settings to default."""
        # Differential Evolution (Default)
        d = defaultSettings.copy()
        if self.__algorithm == AlgorithmType.RGA:
            d.update(GeneticPrams)
        elif self.__algorithm == AlgorithmType.Firefly:
            d.update(FireflyPrams)
        elif self.__algorithm == AlgorithmType.DE:
            d.update(DifferentialPrams)
        self.__set_args(d)
