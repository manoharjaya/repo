# Load CSV using Pandas
import pandas
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
'''
The function returns a pandas.DataFrame that you can immediately start summarizing and plotting.
rest all function like numpy.loadtxt() and csv.reader() will give numpy.arrays as 768*9  and object
'''
data = pandas.read_csv(filename, names=names)
print(data.shape)

print data.head(10)
