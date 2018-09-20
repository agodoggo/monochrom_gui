"""
Created on Fri Sep 19 18:11:40 2014

@author: Bala Krishna Juluri
"""
import visa
import time
import codecs

decode_hex = codecs.getdecoder("hex_codec")
my_instrument = 0

wave1 = 400
wave2 = 600

class Cornerstone260:
    def __init__(my_instrument):
        rm = visa.ResourceManager()
        instrument_list = rm.list_resources()
        print("resources are %s" % instrument_list)
        my_instrument.m = rm.open_resource('ASRL1::INSTR')
        print("instrument selected is %s" % my_instrument.m)
        if my_instrument.m == 0:
            pass
    # def get_nm(my_instrument.m):
    #     my_instrument.m.curr_nm=my_instrument.m.query_ascii_values('?NM')
    #     return my_instrument.m.curr_nm
    def get_serial_model(my_instrument):
        my_instrument.m.write('INFO?')
        return my_instrument.m.read(encoding = 'latin1')
    def get_errortype(my_instrument):
        my_instrument.m.write('ERROR?')
        return my_instrument.m.read()
    def get_error(my_instrument):
        my_instrument.m.write('STB?')
        error = my_instrument.m.read()
        if error == 00:
            return "no error"
        if error == 32:
            return("error occurred, error type is %s" % my_instrument.m.get_errortype())
        else:
             return("no error message, check code")
    def get_units(my_instrument):
        return ("units are in %s" % my_instrument.m.query('UNITS?'))
    def gowave(my_instrument, wavelength):
        my_instrument.m.write('GOWAVE %s' % wavelength)
        print("monochromator moved to %s" % wavelength + "nm")
    def find_wave(my_instrument):
        my_instrument.m.write('WAVE?')
        wavelength = my_instrument.m.read(encoding = 'latin1')
        return ("wavelength is %s" % wavelength)
    def abort(my_instrument):
        my_instrument.m.write('ABORT')
        return "abort executed"
    def spec_units(my_instrument, units):
        my_instrument.m.write('UNITS %s' % units)

if __name__ == "__main__":
    a=Cornerstone260()
    serial_no = a.get_serial_model()
    print(serial_no)
    a.get_units()
    a.gowave(wave1)
    wave_meas1 = a.find_wave()
    print(wave_meas1)
    print("sleeping")
    time.sleep(2)
    print("sleeping over")
    a.gowave(wave2)
    wave_meas2 = a.find_wave()
    print(wave_meas2)
    print(a.get_error())
    print("git commit")

