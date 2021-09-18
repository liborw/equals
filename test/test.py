import datetime
import pint
import numpy as np

ureg = pint.UnitRegistry(auto_reduce_dimensions=True)

def addone(x):
    return x+1

a = 1
b = 3
a + b #= 4
a + a #= 2

addone(a) #= 2

datetime.datetime.now() #=

c = a + b
c #=

a = 10 * ureg('V')
a #=

a = np.array([1, 2, 3])
a * 10 #=


a = np.array([[1, 2, 3],[1,2,3]])
a * 10 #=

