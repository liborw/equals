import datetime
import numpy as np
import pint
ureg = pint.UnitRegistry(auto_reduce_dimensions=True, autoconvert_offset_to_baseunit=True)


def addone(x):
    return x+1


a = 332
b = 9
a + b  #= 341
a + a  #= 664

addone(a)  #= 333

datetime.datetime.now()  #= 2021-09-22 13:24:01.369485

c = a + b + 1
c  #= 342

a = 1 + 3  #= 4

np.array([12,3,4])  #= [12  3  4] # test


test = 10e3 * ureg.V  #= 10000.0 volt
