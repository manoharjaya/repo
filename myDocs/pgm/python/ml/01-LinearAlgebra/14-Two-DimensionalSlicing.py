# split input and output
from numpy import array
# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])

'''
X = [:, :-1] [row,column]
y = [:, -1] [row,only last element]
'''

# separate data
X, y = data[:, :-1], data[:, -1]
print(X)
print(y)
