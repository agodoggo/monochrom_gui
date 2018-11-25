# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Interface_Monochrometer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.initial_wavelength = QtWidgets.QTextBrowser(self.centralwidget)
        self.initial_wavelength.setGeometry(QtCore.QRect(20, 70, 121, 51))
        self.initial_wavelength.setObjectName("initial_wavelength")
        self.initital_wavelength_label = QtWidgets.QLabel(self.centralwidget)
        self.initital_wavelength_label.setGeometry(QtCore.QRect(50, 40, 71, 16))
        self.initital_wavelength_label.setObjectName("initital_wavelength_label")
        self.perform_scan_button = QtWidgets.QPushButton(self.centralwidget)
        self.perform_scan_button.setGeometry(QtCore.QRect(130, 130, 56, 17))
        self.perform_scan_button.setObjectName("perform_scan_button")
        self.final_wavelength = QtWidgets.QTextBrowser(self.centralwidget)
        self.final_wavelength.setGeometry(QtCore.QRect(160, 70, 121, 51))
        self.final_wavelength.setObjectName("final_wavelength")
        self.final_wavelength_label = QtWidgets.QLabel(self.centralwidget)
        self.final_wavelength_label.setGeometry(QtCore.QRect(180, 40, 71, 16))
        self.final_wavelength_label.setObjectName("final_wavelength_label")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(40, 160, 256, 192))
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 231, 16))
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

