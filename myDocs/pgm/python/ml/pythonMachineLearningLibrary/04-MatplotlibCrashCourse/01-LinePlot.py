'''
Matplotlib can be used for creating plots and charts.

The library is generally used as follows:

    Call a plotting function with some data (e.g. plot()).
    Call many functions to setup the properties of the plot (e.g. labels and colors).
    Make the plot visible (e.g. show()).


'''

# The example below creates a simple line plot from one-dimensional data.

# basic line plot
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()
