# Example of LSTM to learn a sequence
from pandas import DataFrame
from pandas import concat
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
# create sequence
length = 10
sequence = [i/float(length) for i in range(length)]
print 'sequence=',sequence
# create X/y pairs
df = DataFrame(sequence)
#print 'df=',df
df = concat([df.shift(1), df], axis=1)
print 'df=',df
df.dropna(inplace=True)
# convert to LSTM friendly format
values = df.values
#print 'values=',values
X, y = values[:, 0], values[:, 1]
print 'X=',X,'y=',y,'len=',len(X),len(y)
X = X.reshape(len(X), 1, 1) # 9,1-----> 9,1,1
#print 'reshape X=',X
# 1. define network
model = Sequential()
model.add(LSTM(10, input_shape=(1,1)))   # this is shape is same as X.reshape(1,1) value (CLEAR)
model.add(Dense(1))
# 2. compile network
model.compile(optimizer='adam', loss='mean_squared_error')
# 3. fit network
history = model.fit(X, y, epochs=1000, batch_size=len(X), verbose=0)
# 4. evaluate network
loss = model.evaluate(X, y, verbose=0)
print(loss)
# 5. make predictions
predictions = model.predict(X, verbose=0)
print(predictions[:, 0])

#------------------CLEAR--------------------
