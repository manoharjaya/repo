# reshape 1D array
from numpy import array
from numpy import reshape
# define array
data = array([11, 22, 33, 44, 55])
print(data.shape)
print data
print
# reshape
data = data.reshape((data.shape[0], 1))
print(data.shape)
print data
