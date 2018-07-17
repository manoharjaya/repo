import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Import Keras Libraries for ANN
import keras
from keras.models import Sequential
from keras.layers import Dense

# Confusion  Matrix
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

#print 'dataset=',dataset

#categorical to Numerical

labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])

print 'X[:,1]=',X[:,1]
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
print 'X[:,2]=',X[:,2]

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

#print 'X=',X


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)

# Perform Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#print 'X_train=',X_train
#print 'X_test=',X_test

classifier = Sequential()
classifier.add(Dense(output_dim = 12, activation = 'relu', input_dim = 11))
classifier.add(Dense(output_dim = 12, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

'''
#Train ANN model
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

classifier.save_weights('weights.h5')
'''

classifier.load_weights("weights.h5")


#Predict model
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)


cm = confusion_matrix(y_test, y_pred)

print cm

