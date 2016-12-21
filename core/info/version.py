# -*- coding: utf-8 -*-
from sys import version_info, argv
import csv, platform
from PyQt5.QtWidgets import QDialog
from .Ui_version import Ui_About_Dialog

version_number = "0.4.0(dev)"

class version_show(QDialog, Ui_About_Dialog):
    def __init__(self, parent=None):
        super(version_show, self).__init__(parent)
        self.setupUi(self)
        self.versionLabel.setText("Pyslvs version "+version_number)

def show_info():
    print("OS Type: "+platform.system())
    print("Python Version: {0:d}.{1:d}.{2:d}".format(*version_info[:3]))
    try:
        from PyQt5.QtCore import qVersion
        print("Qt Version: {0}".format(qVersion().strip()))
    except: print("No Qt5.")
    try:
        from PyQt5.QtCore import PYQT_VERSION_STR as pyqtVersion
        print("PyQt Version:", pyqtVersion.strip())
    except: print("No PyQt5.")
    try:
        from sip import SIP_VERSION_STR as sipVersion
        print("Sip Version:", sipVersion.strip())
    except: print("No Sip.")
    try:
        from PyQt5.Qsci import QSCINTILLA_VERSION_STR as qsciVersion
        print("QScintilla Version:", qsciVersion.strip())
    except: print("No QScintilla.")
    print("-------")

def show_help():
    show_info()
    print("""==Help message==
Arguments:

* python3 launch_pyslvs.py [FileName] [arg1] [arg2] ...

* launch_pyslvs [FileName] [arg1] [arg2] ...

Open a file directly by put file name behind the launch command.

Information and Debug Function:

-v\t--version\tOnly show version infomations and Exit.
-h\t--help\t\tShow this help message and Exit.
-w\t\t\tDon't show Rebuild warning.
--fusion\t\tRun Pyslvs in Fusion style.
--file-data\t\tWhen open a file, show it's data in command line.

Run launch_test.py can start unit test.
================""")

def show_version():
    print("[Pyslvs "+version_number+"]\nPython Version: {0:d}.{1:d}.{2:d}".format(*version_info[:3]))
