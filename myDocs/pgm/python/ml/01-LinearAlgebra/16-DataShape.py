# array shape
from numpy import array
# list of data
data = [[11, 22],
		[33, 44],
		[55, 66]]
# array of data
data = array(data)
print(data.shape)


print('Rows: %d' % data.shape[0])
print('Cols: %d' % data.shape[1])
