from pandas import DataFrame

# binary encode an input pattern, return a list of binary vectors
def encode(pattern, n_unique):
	encoded = list()
	for value in pattern:
		row = [0.0 for x in range(n_unique)]
		row[value] = 1.0
		encoded.append(row)
	return encoded

# create input/output pairs of encoded vectors, returns X, y
def to_xy_pairs(encoded):
	X,y = list(),list()
	for i in range(1, len(encoded)):
		X.append(encoded[i-1])
		y.append(encoded[i])
	return X, y



# convert sequence to x/y pairs ready for use with an LSTM
def to_lstm_dataset(sequence, n_unique):
	# one hot encode
	encoded = encode(sequence, n_unique)
	# convert to in/out patterns
	X,y = to_xy_pairs(encoded)
	#print 'X=',X,'\ny=',y
	# convert to LSTM friendly format
	dfX, dfy = DataFrame(X), DataFrame(y)
	print 'dfX=',dfX,'\ndfy=',dfy
	lstmX = dfX.values   # convert into array CLEAR
	#print 'lstmX=',lstmX
	lstmX = lstmX.reshape(lstmX.shape[0], 1, lstmX.shape[1]) # (4X5) 2D array convert into 3D for lstm 
	lstmY = dfy.values
        #print 'lstmY=',lstmY
	return lstmX, lstmY



seq1 = [3, 0, 1, 2, 3]
seq2 = [4, 0, 1, 2, 4]
n_unique = len(set(seq1 + seq2))

seq1X, seq1Y = to_lstm_dataset(seq1, n_unique)  #  seq1X is 4X1X5 and seq1Y is 4X5 CLEAR for lstm
seq2X, seq2Y = to_lstm_dataset(seq2, n_unique)


print 'seq1X=',seq1X,'\n\nseq1Y=',seq1Y
