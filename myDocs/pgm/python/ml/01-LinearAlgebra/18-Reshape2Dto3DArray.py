# reshape 2D array
from numpy import array
# list of data
data = [[11, 22],
		[33, 44],
		[55, 66]]
# array of data
data = array(data)
print(data.shape)
print data
# reshape
data = data.reshape((data.shape[0], data.shape[1], 1))
print(data.shape)
print data
