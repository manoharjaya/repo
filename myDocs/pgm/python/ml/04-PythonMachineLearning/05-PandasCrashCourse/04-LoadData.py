import pandas as pd
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('dataset/pima-indians-diabetes.data.csv', names=names)

# Describe Data

print(data)

print(data.describe())

# Visualize Data

'''
# Feature Distributions
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'
data.boxplot()

data.hist()

# Feature-Class Relationships
data.groupby('class').hist()

data.groupby('class').plas.hist(alpha=0.4)
# Feature-Feature Relationships

from pandas.plotting import scatter_matrix
scatter_matrix(data, alpha=0.2, figsize=(6, 6), diagonal='kde')

'''

