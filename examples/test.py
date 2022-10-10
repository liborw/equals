import datetime
import numpy as np
import pint
ureg = pint.UnitRegistry(auto_reduce_dimensions=True, autoconvert_offset_to_baseunit=True)
ohm = ureg.ohm


def addone(x):
    return x+1


a = 332
b = 9
a + b  #= 341
a + a  #= 664

addone(a)  #= 333

datetime.datetime.now()  #= 2021-10-01 16:03:58.042935

c = a + b + 1
c  #= 342

a = 1 + 3  #= 4

np.array([12,3,4])  #= [12  3  4] # test


test = 10e6 * ureg.V  #= 10000000.0 volt

#%% Voltage divider

Vin = 45 * ureg.V
R1 = 100e3 * ohm
R2 = 10e3 * ohm
Vout = Vin*R2/(R1 + R2) #= 4.090909090909091 volt
