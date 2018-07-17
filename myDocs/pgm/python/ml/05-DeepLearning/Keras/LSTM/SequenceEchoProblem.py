from random import randint
from numpy import array
from numpy import argmax
from pandas import DataFrame
from pandas import concat
import pandas as pd
# generate a sequence of random numbers in [0, 99]
def generate_sequence(length=25):
	return [randint(0, 99) for _ in range(length)]

# one hot encode sequence
def one_hot_encode(sequence, n_unique=100):
	encoding = list()
	for value in sequence:
		vector = [0 for _ in range(n_unique)]
		vector[value] = 1
		encoding.append(vector)
	return array(encoding)

# decode a one hot encoded string
def one_hot_decode(encoded_seq):
	return [argmax(vector) for vector in encoded_seq]

# convert encoded sequence to supervised learning
def to_supervised(sequence, n_in, n_out):
	# create lag copies of the sequence
	df = DataFrame(sequence)
	#pd.set_option('display.max_columns', 30)
	print 'df=',df.values.shape
	df = concat([df.shift(n_in-i-1) for i in range(n_in)], axis=1) # NOT CLEAR doubt   t-4, t-3 ,t-2 ,t-1, t 
	print df.head(20)
	# drop rows with missing values
	df.dropna(inplace=True)
	# specify columns for input and output pairs
	values = df.values
	print 'len values=',len(values)
	print 'values=',values.shape
	width = sequence.shape[1] #  (25,100)  => 100
	X = values.reshape(len(values), n_in, width)  # 21 , 5 , 100 
	y = values[:, 0:(n_out*width)].reshape(len(values), n_out, width) # 21 , 3 , 100 
	print 'X=',X,'\ny=',y
	return X, y

# generate random sequence
sequence = generate_sequence()
print(sequence)

# one hot encode
encoded = one_hot_encode(sequence)
print 'encoded=',encoded.shape

# convert to X,y pairs
X,y = to_supervised(encoded, 5, 3)

# decode all pairs
for i in range(len(X)):
	print(one_hot_decode(X[i]), '=>', one_hot_decode(y[i]))

# ------------------CLEAR---------------------------

