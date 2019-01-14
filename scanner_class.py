"""
Created on Thurs Nov 20 18:11:40 2014
@author: Agoston Walter

This is where you could troubleshoot the sensor using PyQt5. You can use it in a similar fashion to the monochrometer class. This is unfinished
because the sensor was never able to properly transmit data, so the class will need to be developed for whichever sensor is found.
"""

import pyvisa
import pyvisainstrument
import time
import codecs

class PowerMeter_PM320E:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        instrument_list = rm.list_resources()
        print(str(instrument_list))
        self.p = rm.open_resource('USB0::0x1313::0x8022::M00475920::INSTR')
        # if self.p == 0:
        #     pass

if __name__ == "__main__":
    a = PowerMeter_PM320E()