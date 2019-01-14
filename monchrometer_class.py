"""
Created on Fri Sep 19 18:11:40 2014

@author: Agoston Walter

This is the monochrometer class that I used to test all the possible methods on the monochrometer. I wrote this using the PyVisa package,
documentation can be found online. This is not a final version of a class by any means, just a platform I used to troubleshoot runnning
methods for the monochrometer from. As you will find in the PyVisa documentation, commands to the instrument fall into two possible categories:
queries and commands, and this is how I divide this monochrometer class's methods. At the very end I tested the methods on the monochrometer,
seeing if they worked or not. Of these methods, I found that I only needed the set_wave method for the Wave Scan GUI, so I only took that one
to the final GUI Application window.
"""
import pyvisa
import pyvisainstrument
import time
import codecs

decode_hex = codecs.getdecoder("hex_codec")
self = 0



class Cornerstone260:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        instrument_list = rm.list_resources()
        ##print("resources are %s" % instrument_list)
        self.m = rm.open_resource('ASRL1::INSTR')
        print("instrument selected is %s" % self.m)
        if self.m == 0:
            pass

##
##
##
##      query accessory commands
##
##
##
    def query_shutter(self):
        self.m.write('SHUTTER?')
        return("shutter is %s" % self.m.read())
    def query_filter(self):
        self.m.write('FILTER?')
        return ("filter is %s" % self.m.read())
    def query_filterlabel(self):
        self.m.write("FILTER#LABEL?")
        return('filter label is %s' % self.m.read())
    def query_slit1_microns(self):
        self.m.write("SLIT1MICRONS?")
        return('slit 1 size is %s' % self.m.read() % 'microns')
    def query_slit2_microns(self):
        self.m.write("SLIT2MICRONS?")
        return('slit 2 size is %s' % self.m.read() % 'microns')
    def query_slit3_microns(self):
        self.m.write("SLIT3?")
        return ('slit 3 size is %s' % self.m.read() % 'microns')
    def query_bandpass(self):
        self.m.write("BANDPASS?")
        return ('bandpass is %s' % self.m.read() % 'microns')
    def query_outport(self):
        self.m.write("OUTPORT?")
        return ('outport is %s' % self.m.read())



##
##
##
##      query system commands
##
##
##
    def query_error(self):
        self.m.write('INFO?')
        error = self.m.read()
        if error == 00:
            return "no error"
        if error == 32:
            return("error occurred, error type is %s" % self.m.get_errortype())
        else:
             return("no error message, check code")
    def query_errortype(self):
        self.m.write('ERROR?')
        return self.m.read()
    def query_info(self):
        return(self.m.query('INFO?'))
        ##return self.m.read(encoding = 'latin1')
    def query_handshake(self):
        self.m.write('HANDSHAKE?')
        return self.m.read()
    def query_address(self):
        self.m.write('ADDRESS?')
        return self.m.read()

    def set_address(self, XX):
        self.m.write('ADDRESS %s' % XX)
        return "ADDRESS changed to %s" % XX
    def set_handshake(self, X):
        self.m.write('HANDSHAKE %s' % X)
        return self.m.read()

##
##
##
##      query motion commands
##
##
##
    def query_units(self):
        return self.m.query("UNITS?")

    def query_wave(self):
        return self.m.query("WAVE?")
        ##
        # return ("monochromator moved to %s" % self.m.read() %  "nm")

    def query_calibrate(self):
        self.m.write('CALIBRATE?')
        return "current position defined as wavelength: %s" % self.m.read()

    def query_step(self):
        self.m.write('STEP?' )
        return "wavelength drive moved by %s" % self.m.read()
##
##
##
##      query grating commands
##
##


    def query_grating(self):
        self.m.write('GRAT?')
        return ("grating info (grating number, lines/mm, label): %s" % self.m.read())

    def query_grat1_label(self):
        self.m.write('GRAT1LABEL?')
        return ("grating 1 label is %s" % self.m.read() % "nm")
    def query_grat2_label(self):
        return self.m.query('GRAT2LABEL?')
       ##return ("grating 2 label is %s" % self.m.read() % "nm")
    def query_grat3_label(self):
        self.m.write('GRAT3LABEL?')
        return ("grating 3 label is %s" % self.m.read() % "nm")

    def query_grat1_lines(self):
        self.m.write('GRAT1LINES?')
        return ("grating 1 lines/mm is %s" % self.m.read() + "nm")
    def query_grat2_lines(self):
        self.m.write('GRAT2LINES?')
        return ("grating 2 lines/mm is %s" % self.m.read() + "nm")
    def query_grat3_lines(self):
        self.m.write('GRAT3LINES?')
        return ("grating 3 lines/mm is %s" % self.m.read() + "nm")

    def query_grat1factor(self):
        self.m.write('GRAT1FACTOR?')
        return ("calibration factor of grating 1 is %s" % self.m.read() + "nm")
    def query_grat2factor(self):
        self.m.write('GRAT2FACTOR?')
        return ("calibration factor of grating 2 is %s" % self.m.read() + "nm")
    def query_grat3factor(self):
        self.m.write('GRAT3FACTOR?')
        return ("calibration factor of grating 3 is %s" % self.m.read() + "nm")

    def query_grat1offset(self):
        self.m.write('GRAT1OFFSET?')
        return ("calibration offset of grating 1 is %s" % self.m.read() + "nm")
    def query_grat2offset(self):
        self.m.write('GRAT2OFFSET?')
        return ("calibration offset of grating 2 is %s" % self.m.read() + "nm")
    def query_grat3offset(self):
        self.m.write('GRAT3OFFSET?')
        return ("calibration offset of grating 3 is %s" % self.m.read() + "nm")

    def query_grat1zero(self):
        self.m.write('GRAT1ZERO?')
        return ("zero of grating 1 is %s" % self.m.read() % "nm")
    def query_grat2zero(self):
        self.m.write('GRAT2ZERO?')
        return ("zero of grating 2 is %s" % self.m.read() % "nm")
    def query_grat3zero(self):
        self.m.write('GRAT3ZERO %s')
        return ("zero of grating 3 is %s" % self.m.read() % "nm")

##
##
##
##      SET accessory commands
##
##
##
##    def set_shutter(self, bool):
##        if bool == "open":
##            self.m.write('SHUTTER T')
##        else if bool = "shut":
##            self.m.write('SHUTTER C')
##        return ("shutter set to %s" % self.m.read())

    def set_filter(self, X):
        self.m.write('FILTER %s' % X)
        return ("filter set to %s" % self.m.read())

    def set_filterlabel(self, TTTTTTTT):
        self.m.write("FILTER#LABEL" % TTTTTTTT)
        return ('filter label set to %s' % TTTTTTTT)

    def set_slit1_microns(self, XXXX):
        self.m.write("SLIT1MICRONS %s" % XXXX)
        return ('slit 1 size set to %s' % XXXX % 'microns')

    def set_slit2_microns(self, XXXX):
        self.m.write("SLIT2MICRONS %s" % XXXX)
        return ('slit 2 size set to %s' % XXXX % 'microns')

    def set_slit3_microns(self, XXXX):
        self.m.write("SLIT3 %s" % XXXX)
        return ('slit 3 size set to %s' % XXXX % 'microns')

    def set_bandpass(self, XXXXX):
        self.m.write("BANDPASS %s" % XXXXX)
        return ('bandpass set to %s' % XXXXX % 'microns')

    def set_outport(self, X):
        self.m.write("OUTPORT %s" % X)
        return ('outport set to %s' % X)



##
##
##
##      set motion commands
##
##
##


    def set_units(self, TT):
        self.m.write('UNITS %s' % TT)
    def set_wave(self, wavelength):
        self.m.write('GOWAVE %s' % wavelength)
        return ("monochromator moved to %s" % wavelength + "nm")
    def set_calibrate(self, XXXXXX):
        self.m.write('CALIBRATE %s' % XXXXXX)
        return "current position defined as wavelength: %s" % XXXXXX
    def set_abort(self):
        self.m.write('ABORT')
        return "abort executed"
    def set_step(self, XXXX):
        self.m.write('STEP %s' % XXXX)
        return "wavelength drive moved by %s" % XXXX




##
##
##
##      set grating commands
##
##
##

    def set_grating(self, grating):
        self.m.write('GRAT %s' % grating)
        return("grating set to %s" % grating + "#")

    def set_grat1_label(self, TTTTTTTT):
        self.m.write('GRAT1LABEL %s' % TTTTTTTT)
        return("grating 1 label set to %s" % TTTTTTTT + "nm")
    def set_grat2_label(self, TTTTTTTT):
        self.m.write('GRAT2LABEL %s' % TTTTTTTT)
        return("grating 2 label set to %s" % TTTTTTTT + "nm")
    def set_grat3_label(self, TTTTTTTT):
        self.m.write('GRAT3LABEL %s' % TTTTTTTT)
        return("grating 3 label set to %s" % TTTTTTTT + "nm")

    def set_grat1_lines(self, XXXX):
        self.m.write('GRAT1LINES %s' % XXXX)
        return("grating 1 lines/mm set to %s" % XXXX + "nm")
    def set_grat2_lines(self, XXXX):
        self.m.write('GRAT2LINES %s' % XXXX)
        return("grating 2 lines/mm set to %s" % XXXX + "nm")
    def set_grat3_lines(self, XXXX):
        self.m.write('GRAT3LINES %s' % XXXX)
        return("grating 3 lines/mm set to %s" % XXXX + "nm")

    def set_grat1factor(self, XXXXXX):
        self.m.write('GRAT1FACTOR %s' % XXXXXX)
        return ("calibration factor of grating 1 set to %s" % XXXXXX + "nm")
    def set_grat2factor(self, XXXXXX):
        self.m.write('GRAT2FACTOR %s' % XXXXXX)
        return ("calibration factor of grating 2 set to %s" % XXXXXX + "nm")
    def set_grat3factor(self, XXXXXX):
        self.m.write('GRAT3FACTOR %s' % XXXXXX)
        return ("calibration factor of grating 3 set to %s" % XXXXXX + "nm")

    def set_grat1offset(self, XXXXXX):
        self.m.write('GRAT1OFFSET %s' % XXXXXX)
        return ("calibration offset of grating 1 set to %s" % XXXXXX + "nm")
    def set_grat2offset(self, XXXXXX):
        self.m.write('GRAT2OFFSET %s' % XXXXXX)
        return ("calibration offset of grating 2 set to %s" % XXXXXX + "nm")
    def set_grat3offset(self, XXXXXX):
        self.m.write('GRAT3OFFSET %s' % XXXXXX)
        return ("calibration offset of grating 3 set to %s" % XXXXXX + "nm")

    def set_grat1zero(self, XXXXXX):
        self.m.write('GRAT1ZERO %s' % XXXXXX)
        return ("zero of grating 1 set to %s" % XXXXXX + "nm")
    def set_grat2zero(self, XXXXXX):
        self.m.write('GRAT2ZERO %s' % XXXXXX)
        return ("zero of grating 2 set to %s" % XXXXXX + "nm")
    def set_grat3zero(self, XXXXXX):
        self.m.write('GRAT3ZERO %s' % XXXXXX)
        return ("zero of grating 3 set to %s" % XXXXXX + "nm")



if __name__ == "__main__":
    wave1 = 100
    wave2 = 2000
    a = Cornerstone260()
    serial_no = a.query_info()
    print(serial_no)
    a.query_units()
    a.set_wave(wave1)
    wave_meas1 = a.query_wave()
    print(wave_meas1)
    print("sleeping")
    time.sleep(2)
    print("sleeping over")
    a.set_wave(wave2)
    wave_meas2 = a.query_wave()
    print(wave_meas2)
    print(a.query_error())
    print("git commit push")

