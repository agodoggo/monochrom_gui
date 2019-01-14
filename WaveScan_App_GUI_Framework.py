"""
Created on Thurs Nov 20 18:11:40 2014
@author: Agoston Walter

This is the GUI coding in Python. This is all done using the PyQt5 package, if you want to learn you can read documentation online
and refer to tutorials, this is how I learned how to use it. It was created from the GUI_mono UI file in this folder using the pyuic5 command.
You can look up how to use this command to convert ui files into python files in the terminal.
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_mono.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.initial_wavelength = QtWidgets.QTextEdit(self.centralwidget)
        self.initial_wavelength.setGeometry(QtCore.QRect(20, 130, 121, 51))
        self.initial_wavelength.setObjectName("initial_wavelength")
        self.initital_wavelength_label = QtWidgets.QLabel(self.centralwidget)
        self.initital_wavelength_label.setGeometry(QtCore.QRect(20, 100, 200, 20))
        self.initital_wavelength_label.setObjectName("initital_wavelength_label")
        self.perform_scan_button = QtWidgets.QPushButton(self.centralwidget)
        self.perform_scan_button.setGeometry(QtCore.QRect(210, 150, 120, 25))
        self.perform_scan_button.setObjectName("perform_scan_button")
        self.final_wavelength = QtWidgets.QTextEdit(self.centralwidget)
        self.final_wavelength.setGeometry(QtCore.QRect(400, 130, 121, 51))
        self.final_wavelength.setObjectName("final_wavelength")
        self.final_wavelength_label = QtWidgets.QLabel(self.centralwidget)
        self.final_wavelength_label.setGeometry(QtCore.QRect(400, 100, 200, 20))
        self.final_wavelength_label.setObjectName("final_wavelength_label")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(240, 220, 200, 20))
        self.result_label.setObjectName("final_wavelength_label")
        self.result = QtWidgets.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(140, 250, 256, 192))
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.initital_wavelength_label.setText(_translate("MainWindow", "Initial Wavelength"))
        self.perform_scan_button.setText(_translate("MainWindow", "Perform Scan"))
        self.final_wavelength_label.setText(_translate("MainWindow", "Final Wavelength"))
        self.label.setText(_translate("MainWindow", "Spectroscopy Experiment GUI"))
        self.result_label.setText(_translate("MainWindow", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

