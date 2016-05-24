import numpy as np
from StringIO import StringIO

a = np.genfromtxt('temperaturetest.txt', delimiter=",", dtype=None)
print(a)