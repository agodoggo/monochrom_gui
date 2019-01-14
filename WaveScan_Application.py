"""
Created on Thurs Nov 20 18:11:40 2014
@author: Agoston Walter

This is the app to run from the GUI from.
It imports the GUI from the test1gui.py file and then you can write methods for the GUI.
The Monochromator set_wave function works, but one has to add the sensor method to read the wavelengths' power and displaya graph.
The PM320E did not work with the S401C sensor, so I was unable to write this method of creating the graph because the sensor could not read the data.
When you write the method, please write it in the Create_Spectral_Graph method, the method currently just changes the monochromator to the specified wavelengths
and then prints your finals wavelength into the results textbox.

I built this app using the Python packages PyVisa and PyQt. To learn how to use these packages please refer to the bookmarks in Firefox or look
up tutorials online, they are quite helpful. A tip for PyVisa: the commands used to control the instruments can be found in the instrument
manuals, the rest of the methods are defined in the PyVisa documentation. I found StackOverflow to be a helpful resource too.
"""
import pyvisa
import pyvisainstrument
import time
import codecs

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from WaveScan_App_GUI_Framework import Ui_MainWindow

class AppWindow(QMainWindow):

    def __init__(self):
        rm = pyvisa.ResourceManager()
        #this opens the monochrometer
        self.m = rm.open_resource('ASRL1::INSTR')
        print(self.m)
        if self.m == 0:
            pass

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        #Makes the button display the graph if clicked upon
        self.ui.perform_scan_button.clicked.connect(lambda: self.Create_Spectral_Graph())
        self.show()

    #Method to change: this prints out the final graph of the data from the sensor when you click on the printresults button
    def Create_Spectral_Graph(self):
         init_wave = int(self.ui.initial_wavelength.toPlainText())
         self.set_wave(init_wave)
         time.sleep(5)
         final_wave = int(self.ui.final_wavelength.toPlainText())
         self.set_wave(final_wave)
         self.ui.result.setText(str(final_wave))

    #method to change wavelength on monochromator
    def set_wave(self, wavelength):
        self.m.write('GOWAVE %s' % wavelength)
        return ("monochromator moved to %s" % wavelength + "nm")


    #possible future methods

    # def query_power(self):
    #     #self.write(':POW[1]:VAL?')
    #     return("querying power value (W)")
    #
    #
    # def init_measurement(self):
    #     #self.write(':MEAS : INIT[1]')
    #     return ("sensor inititated measurement")
    #
    # def abort_measurement(self):
    #     #self.write(':MEAS : ABORT[1]')
    #     return ("sensor aborted measurement")

#runs the application
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())