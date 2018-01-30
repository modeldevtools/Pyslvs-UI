# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/synthesis/DimensionalSynthesis/Algorithm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 617)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/DimensionalSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_main = QtWidgets.QSplitter(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_main.sizePolicy().hasHeightForWidth())
        self.splitter_main.setSizePolicy(sizePolicy)
        self.splitter_main.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_main.setObjectName("splitter_main")
        self.splitter_right = QtWidgets.QSplitter(self.splitter_main)
        self.splitter_right.setOrientation(QtCore.Qt.Vertical)
        self.splitter_right.setObjectName("splitter_right")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_right)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.profile_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.profile_name.setReadOnly(True)
        self.profile_name.setObjectName("profile_name")
        self.horizontalLayout_7.addWidget(self.profile_name)
        self.load_profile = QtWidgets.QToolButton(self.groupBox_2)
        self.load_profile.setObjectName("load_profile")
        self.horizontalLayout_7.addWidget(self.load_profile)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.Expression = QtWidgets.QLineEdit(self.groupBox_2)
        self.Expression.setReadOnly(True)
        self.Expression.setObjectName("Expression")
        self.horizontalLayout_17.addWidget(self.Expression)
        self.Expression_copy = QtWidgets.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Expression_copy.setIcon(icon1)
        self.Expression_copy.setObjectName("Expression_copy")
        self.horizontalLayout_17.addWidget(self.Expression_copy)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.Link_Expression = QtWidgets.QLineEdit(self.groupBox_2)
        self.Link_Expression.setReadOnly(True)
        self.Link_Expression.setObjectName("Link_Expression")
        self.horizontalLayout_18.addWidget(self.Link_Expression)
        self.Link_Expression_copy = QtWidgets.QPushButton(self.groupBox_2)
        self.Link_Expression_copy.setIcon(icon1)
        self.Link_Expression_copy.setObjectName("Link_Expression_copy")
        self.horizontalLayout_18.addWidget(self.Link_Expression_copy)
        self.verticalLayout_6.addLayout(self.horizontalLayout_18)
        self.ground_joints = QtWidgets.QTableWidget(self.groupBox_2)
        self.ground_joints.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ground_joints.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ground_joints.setObjectName("ground_joints")
        self.ground_joints.setColumnCount(5)
        self.ground_joints.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ground_joints.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ground_joints.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ground_joints.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ground_joints.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ground_joints.setHorizontalHeaderItem(4, item)
        self.verticalLayout_6.addWidget(self.ground_joints)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_right)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pointNum = QtWidgets.QLabel(self.horizontalWidget)
        self.pointNum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pointNum.setObjectName("pointNum")
        self.horizontalLayout_2.addWidget(self.pointNum)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Point_list = QtWidgets.QListWidget(self.horizontalWidget)
        self.Point_list.setObjectName("Point_list")
        self.verticalLayout_2.addWidget(self.Point_list)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.clearAll = QtWidgets.QPushButton(self.horizontalWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearAll.setIcon(icon2)
        self.clearAll.setAutoDefault(False)
        self.clearAll.setObjectName("clearAll")
        self.horizontalLayout_19.addWidget(self.clearAll)
        self.close_path = QtWidgets.QPushButton(self.horizontalWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/freemove_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_path.setIcon(icon3)
        self.close_path.setObjectName("close_path")
        self.horizontalLayout_19.addWidget(self.close_path)
        self.pathAdjust = QtWidgets.QToolButton(self.horizontalWidget)
        self.pathAdjust.setObjectName("pathAdjust")
        self.horizontalLayout_19.addWidget(self.pathAdjust)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.line_5 = QtWidgets.QFrame(self.horizontalWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.series = QtWidgets.QPushButton(self.horizontalWidget)
        self.series.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/formula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.series.setIcon(icon4)
        self.series.setAutoDefault(False)
        self.series.setObjectName("series")
        self.horizontalLayout.addWidget(self.series)
        self.importCSV = QtWidgets.QPushButton(self.horizontalWidget)
        self.importCSV.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/CSV.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importCSV.setIcon(icon5)
        self.importCSV.setIconSize(QtCore.QSize(20, 20))
        self.importCSV.setObjectName("importCSV")
        self.horizontalLayout.addWidget(self.importCSV)
        self.importXLSX = QtWidgets.QPushButton(self.horizontalWidget)
        self.importXLSX.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/excel_2013.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importXLSX.setIcon(icon6)
        self.importXLSX.setIconSize(QtCore.QSize(20, 20))
        self.importXLSX.setObjectName("importXLSX")
        self.horizontalLayout.addWidget(self.importXLSX)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_6 = QtWidgets.QFrame(self.horizontalWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.moveUp = QtWidgets.QPushButton(self.horizontalWidget)
        self.moveUp.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveUp.setIcon(icon7)
        self.moveUp.setAutoDefault(False)
        self.moveUp.setObjectName("moveUp")
        self.verticalLayout_3.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QPushButton(self.horizontalWidget)
        self.moveDown.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveDown.setIcon(icon8)
        self.moveDown.setAutoDefault(False)
        self.moveDown.setObjectName("moveDown")
        self.verticalLayout_3.addWidget(self.moveDown)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addWidget(self.horizontalWidget)
        self.splitter_left = QtWidgets.QSplitter(self.splitter_main)
        self.splitter_left.setOrientation(QtCore.Qt.Vertical)
        self.splitter_left.setObjectName("splitter_left")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.splitter_left)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.verticalGroupBox)
        self.horizontalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Result_list = QtWidgets.QListWidget(self.verticalGroupBox)
        self.Result_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Result_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Result_list.setObjectName("Result_list")
        self.verticalLayout_13.addWidget(self.Result_list)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Result_load_settings = QtWidgets.QPushButton(self.verticalGroupBox)
        self.Result_load_settings.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/dataupdate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Result_load_settings.setIcon(icon9)
        self.Result_load_settings.setObjectName("Result_load_settings")
        self.horizontalLayout_10.addWidget(self.Result_load_settings)
        self.Result_chart = QtWidgets.QPushButton(self.verticalGroupBox)
        self.Result_chart.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Result_chart.setIcon(icon10)
        self.Result_chart.setObjectName("Result_chart")
        self.horizontalLayout_10.addWidget(self.Result_chart)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.deleteButton = QtWidgets.QPushButton(self.verticalGroupBox)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_10.addWidget(self.deleteButton)
        self.mergeButton = QtWidgets.QPushButton(self.verticalGroupBox)
        self.mergeButton.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mergeButton.setIcon(icon11)
        self.mergeButton.setObjectName("mergeButton")
        self.horizontalLayout_10.addWidget(self.mergeButton)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.splitter_left)
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.type0 = QtWidgets.QRadioButton(self.verticalGroupBox_2)
        self.type0.setChecked(False)
        self.type0.setObjectName("type0")
        self.verticalLayout_4.addWidget(self.type0)
        self.type1 = QtWidgets.QRadioButton(self.verticalGroupBox_2)
        self.type1.setObjectName("type1")
        self.verticalLayout_4.addWidget(self.type1)
        self.type2 = QtWidgets.QRadioButton(self.verticalGroupBox_2)
        self.type2.setChecked(True)
        self.type2.setObjectName("type2")
        self.verticalLayout_4.addWidget(self.type2)
        self.advanceButton = QtWidgets.QPushButton(self.verticalGroupBox_2)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.advanceButton.setIcon(icon12)
        self.advanceButton.setObjectName("advanceButton")
        self.verticalLayout_4.addWidget(self.advanceButton)
        self.line_3 = QtWidgets.QFrame(self.verticalGroupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.label_7 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.timeShow = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.timeShow.setObjectName("timeShow")
        self.verticalLayout_4.addWidget(self.timeShow)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.splitter_main)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timePanel = QtWidgets.QWidget(Form)
        self.timePanel.setObjectName("timePanel")
        self.timePanelLayout = QtWidgets.QHBoxLayout(self.timePanel)
        self.timePanelLayout.setContentsMargins(6, 0, 6, 0)
        self.timePanelLayout.setObjectName("timePanelLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.timePanel)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.portText = QtWidgets.QLineEdit(self.timePanel)
        self.portText.setObjectName("portText")
        self.horizontalLayout_9.addWidget(self.portText)
        self.timePanelLayout.addLayout(self.horizontalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timePanelLayout.addItem(spacerItem4)
        self.GenerateZMQ = QtWidgets.QPushButton(self.timePanel)
        self.GenerateZMQ.setEnabled(False)
        self.GenerateZMQ.setMinimumSize(QtCore.QSize(120, 0))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/ZeroMQ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GenerateZMQ.setIcon(icon13)
        self.GenerateZMQ.setAutoDefault(True)
        self.GenerateZMQ.setObjectName("GenerateZMQ")
        self.timePanelLayout.addWidget(self.GenerateZMQ)
        self.GenerateLocal = QtWidgets.QPushButton(self.timePanel)
        self.GenerateLocal.setEnabled(False)
        self.GenerateLocal.setMinimumSize(QtCore.QSize(120, 0))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/local.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GenerateLocal.setIcon(icon14)
        self.GenerateLocal.setAutoDefault(True)
        self.GenerateLocal.setObjectName("GenerateLocal")
        self.timePanelLayout.addWidget(self.GenerateLocal)
        self.horizontalLayout_4.addWidget(self.timePanel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_2.setTitle(_translate("Form", "Profile"))
        self.load_profile.setText(_translate("Form", "..."))
        item = self.ground_joints.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.ground_joints.horizontalHeaderItem(1)
        item.setText(_translate("Form", "x"))
        item = self.ground_joints.horizontalHeaderItem(2)
        item.setText(_translate("Form", "y"))
        item = self.ground_joints.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Range"))
        item = self.ground_joints.horizontalHeaderItem(4)
        item.setText(_translate("Form", "type"))
        self.groupBox.setTitle(_translate("Form", "Path"))
        self.pointNum.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">0</span></p></body></html>"))
        self.clearAll.setStatusTip(_translate("Form", "Clear all points."))
        self.close_path.setStatusTip(_translate("Form", "Close the path."))
        self.pathAdjust.setStatusTip(_translate("Form", "Process path data, such as moving or scaling."))
        self.pathAdjust.setText(_translate("Form", "..."))
        self.series.setToolTip(_translate("Form", "Formula"))
        self.series.setStatusTip(_translate("Form", "Generat points from formula."))
        self.importCSV.setToolTip(_translate("Form", "CSV"))
        self.importCSV.setStatusTip(_translate("Form", "Import path from CSV format."))
        self.importXLSX.setToolTip(_translate("Form", "Microsoft Excel"))
        self.importXLSX.setStatusTip(_translate("Form", "Import path from Microsoft Excel format."))
        self.verticalGroupBox.setTitle(_translate("Form", "Results"))
        self.Result_load_settings.setStatusTip(_translate("Form", "Load the setting of this result."))
        self.Result_chart.setStatusTip(_translate("Form", "Show the fitness - time chart"))
        self.deleteButton.setStatusTip(_translate("Form", "Delete this result."))
        self.mergeButton.setStatusTip(_translate("Form", "Merge this result to canvas."))
        self.verticalGroupBox_2.setTitle(_translate("Form", "Options"))
        self.type0.setText(_translate("Form", "Genetic Algorithm"))
        self.type1.setText(_translate("Form", "Firefly Algorithm"))
        self.type2.setText(_translate("Form", "Differential Evolution"))
        self.advanceButton.setText(_translate("Form", "Advance ..."))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Time spent: </span></p></body></html>"))
        self.timeShow.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">[N/A]</span></p></body></html>"))
        self.label.setText(_translate("Form", "ZMQ filter: "))
        self.portText.setStatusTip(_translate("Form", "LAN screening."))
        self.portText.setText(_translate("Form", "tcp://*:8000"))
        self.GenerateZMQ.setStatusTip(_translate("Form", "Calculated by the zmq servers."))
        self.GenerateZMQ.setText(_translate("Form", "Synthesis"))
        self.GenerateLocal.setStatusTip(_translate("Form", "Calculated on the local side."))
        self.GenerateLocal.setText(_translate("Form", "Synthesis"))

import icons_rc
import preview_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

