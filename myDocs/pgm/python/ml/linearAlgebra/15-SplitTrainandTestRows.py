# split train and test
from numpy import array
# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])
print data
print
# separate data
split = 2
train,test = data[:split,:],data[split:,:]
print(train)
print
print(test)
