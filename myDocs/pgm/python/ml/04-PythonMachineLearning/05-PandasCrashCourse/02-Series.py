#  A series is a one-dimensional array where the rows and columns can be labeled.

# series
import numpy
import pandas
myarray = numpy.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)

# You can access the data in a series like a NumPy array and like dictionary, for example:

print(myseries[0])
print(myseries['a'])
