# A data frame is a multi-dimensional array where the rows and the columns can be labeled.

# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

# Data can be index using column names.
print "------------------------------------------------"
print(" column= %s" % mydataframe['one'])
print(" column= %s" % mydataframe.two)
