# Gaussian Naive Bayes Classification
import pandas
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
url='dataset/pima-indians-diabetes.data.csv'
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
seed = 7
kfold = model_selection.KFold(n_splits=10, random_state=seed)
model = GaussianNB()
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
