#Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Read dataset
dataset = pd.read_csv('customerhire.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:,3].values

print x
print '\n'
print y

#Missing Values
from sklearn.preprocessing import Imputer

imputer = Imputer (missing_values= 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:,1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])


print '\n'

print x

#Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
x[:, 0] = labelEncoder_X.fit_transform(x[:, 0])
print 'label encoder=',x
oneHotEncoder = OneHotEncoder(categorical_features=[0])
print 'oneHotEncoder=',oneHotEncoder
x = oneHotEncoder.fit_transform(x).toarray()
print 'x=',x
labelEncoder_Y = LabelEncoder()
y = labelEncoder_Y.fit_transform(y)

print 'y lable=',y


#Splitting Dataset into Training set and Test set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
