# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
import pandas
import numpy
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
url = "dataset/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
print dataframe
print '-----------------------------------'
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
#print Y
scaler = StandardScaler().fit(X)
#print "s=",scaler
rescaledX = scaler.transform(X)
print "rs=",rescaledX
#summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
