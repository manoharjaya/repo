# Pairwise Pearson correlations
import pandas
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
url='dataset/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
correlations = data.corr(method='pearson')
print(correlations)
