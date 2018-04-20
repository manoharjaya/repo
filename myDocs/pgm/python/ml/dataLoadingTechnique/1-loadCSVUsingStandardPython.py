# Load CSV (using python)
import csv
import numpy
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data)

#reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
#print reader
x = list(reader)
#print x
'''
list of  list in normal list
'''
l1=list()
for row in x:
	l1.append(row)

print l1[0]
print
'''
The example loads an object that can iterate over each row of the data and can easily be converted into a NumPy array
'''
data = numpy.array(x).astype('float')
print(data.shape)

print data
