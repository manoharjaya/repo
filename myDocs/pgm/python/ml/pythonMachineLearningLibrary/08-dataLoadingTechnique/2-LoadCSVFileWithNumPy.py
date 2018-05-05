# Load CSV
import numpy
from urllib2 import urlopen # python 2.7 issue fixed by manohar

filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rt')

#url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
#raw_data = urlopen(url)

data = numpy.loadtxt(raw_data, delimiter=",")
print(data.shape)
print data[0]
print numpy.ndarray
