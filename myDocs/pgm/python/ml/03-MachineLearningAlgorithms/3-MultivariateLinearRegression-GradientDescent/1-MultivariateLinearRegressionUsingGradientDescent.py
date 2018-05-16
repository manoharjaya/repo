

# Make a prediction with coefficients
def predict(row, coefficients):
	yhat = coefficients[0]  # 0.0 2) 0.01  3) 0.03
	for i in range(len(row)-1):
		yhat += coefficients[i + 1] * row[i]   # 0.0+0.0*1  2) 0.01+0.01*2   3) 0.03+0.06*4 
	return yhat

# Estimate linear regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
	coef = [0.0 for i in range(len(train[0]))]  # [1,1] 
	# print "coef",coef   #[0.0 0.0]
	for epoch in range(n_epoch):  # 5
		sum_error = 0
		for row in train:
			yhat = predict(row, coef)   # 0  2) 0.03  
			error = yhat - row[-1]      # 0-1=> -1    2)0.03-3=>  -2.97
			sum_error += error**2      # 1  2) 1+8.82 => 9.82  3) 7.45+9.82 =>17.27
			coef[0] = coef[0] - l_rate * error   # 0.0-0.01*(-1) => 0.01  2) 0.01-0.01*(-2.97)  => 0.03
			for i in range(len(row)-1):   
				coef[i + 1] = coef[i + 1] - l_rate * error * row[i]   #  = 0.0-0.01*(-1)*1 => 0.01  2) 0.01-0.01*(-2.97)*2  => 0.06
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
		#print "coef=",coef
	return coef

# Calculate coefficients
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
l_rate = 0.001
n_epoch = 50    # 1 epoch gives 5 iteration ie.5*5 => 25 
coef = coefficients_sgd(dataset, l_rate, n_epoch) 
print(coef)
