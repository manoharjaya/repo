# Linear Regression With Stochastic Gradient Descent for Wine Quality
from random import seed
from random import randrange
from csv import reader
from math import sqrt

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:   # 
		csv_reader = reader(file)       # 7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8,6
		for row in csv_reader:          
			if not row:
				continue
			dataset.append(row)   #[[7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8,6],....]
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:  #7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8,6
		row[column] = float(row[column].strip())    # row[0]=['7,0']=[7.0]

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])): #len([7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8,6])=12
		col_values = [row[i] for row in dataset] # col_values=[[7.0],[6.3],[8.1]]
		value_min = min(col_values)   # value_min=6.3
		value_max = max(col_values)  # value_max=8.1
		minmax.append([value_min, value_max])   # minmax = [[[6.3],[8.1]],[]]
	return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset) # dataset
	# print "dataset_copy=",len(dataset_copy)  #dataset_copy= 4898
						 #fold_size= 979
	fold_size = int(len(dataset) / n_folds)
	# print "fold_size=",fold_size
	for i in range(n_folds):  # 5 
		fold = list()
		while len(fold) < fold_size:  # 0 < 979
			index = randrange(len(dataset_copy))  # take random no from len(dataset_copy)
			fold.append(dataset_copy.pop(index))   # take particular list add into fold  [[[1],[2],[3]...[979]] , [[1],[2],[3],....[979]] , [[1],[2],[3],....[979]] , [[1],[2],[3],....[979]] , [[1],[2],[3],....[979]]]
		# print "fold=",fold
		dataset_split.append(fold)  
		# print "%d fold last data\n"%(i+1),fold[-1]

	# print "check=",dataset_split
	# print "check=",dataset_split[0]
	
	return dataset_split

# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

# Evaluate an algorithm using a cross validation split
# we remove one fold from train_set that is to act as test_set   
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	# print "len(folds)=",len(folds)
	# print "before =",folds[-1]  # last fold contains folds[-1]=[[],[].....979] 979 rows 
	for fold in folds:  # [[0.21153846153846159, 0.34313725490196073, 0.20481927710843376, 0.10736196319018404, 0.10682492581602374, 0.080139372822299645, 						0.25290023201856149, 0.098515519568150203, 0.28181818181818158, 0.17441860465116277, 0.48387096774193555, 0.5],....]  
		train_set = list(folds)  # train_set = list(5) 
        # print train_set
		train_set.remove(fold)   #  remove perticular fold from the train_set 
		# print "train_set=",train_set
		train_set = sum(train_set, [])  #  remove 5 folds into one eg. [[1],[2],[3]...[979] , [1],[2],[3],....[979] , [1],[2],[3],....[979] , [1],[2],[3],....[979] , [1],[2],[3],....[979]]
		# everthing in s convert [[1], [2], [3], [4], [5]] into  [1, 2, 3, 4, 5] => 15 and take whole dataset except one row and  sum whole data into single row
		# print "---------------------------------"
		# print "after train_set=",train_set 
		# print "---------------------------------"
		test_set = list()  
		# print "fold=",fold
		for row in fold:  # take first value from fold = 0.21153846153846159
			# print "row=",row
			# print "row size=",len(row)
			
			row_copy = list(row)  # 
			#print "list(row)=",row  # [0.22115384615384617, 0.22549019607843135, 0.15662650602409639, 0.024539877300613498, 0.12462908011869436, 0.090592334494773524, 0.36658932714617171, 0.10584152689415843, 0.59090909090909105, 0.29069767441860461, 0.38709677419354849, 0.5]


			test_set.append(row_copy)  # test_set = [[0.21153846153846159,,,,,,,,,,None],[],[]]
			
			row_copy[-1] = None    # row_copy=[0.21153846153846159,,,,,,,,,,,None]  
			# print "test_set=",test_set[0]
			# print "row_copy=",row_copy  

		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		rmse = rmse_metric(actual, predicted)
		scores.append(rmse)
	return scores

# Make a prediction with coefficients
def predict(row, coefficients):   
	yhat = coefficients[0]
	for i in range(len(row)-1):    # last value will be None in dataset
		yhat += coefficients[i + 1] * row[i]
	return yhat

# Estimate linear regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
	coef = [0.0 for i in range(len(train[0]))] # coef=[0.0,0.0,,,,,,,,,]
	#print "coef=",len(coef) # 12
	#print "coef=",coef[-1]
	for epoch in range(n_epoch): 
		for row in train:
			# print "row=",row[-1]  #   0.5 
			yhat = predict(row, coef)
			error = yhat - row[-1]
			# print "error=",error   # -0.5
			coef[0] = coef[0] - l_rate * error
			for i in range(len(row)-1):
				coef[i + 1] = coef[i + 1] - l_rate * error * row[i]
			# print(l_rate, n_epoch, error)
	return coef

# Linear Regression Algorithm With Stochastic Gradient Descent
def linear_regression_sgd(train, test, l_rate, n_epoch):
	predictions = list()
	coef = coefficients_sgd(train, l_rate, n_epoch)
	for row in test:
		yhat = predict(row, coef)
		predictions.append(yhat)
	return(predictions)

# Linear Regression on wine quality dataset
seed(1)
# load and prepare data
# filename = '/home/manohar/Downloads/winequality-white.csv'
filename = 'dataset/winequality-white.csv'

dataset = load_csv(filename)
for i in range(len(dataset[0])):   # len([7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8,6]) => range(12)
	str_column_to_float(dataset, i) # (dataset,0)
# normalize
minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)
# evaluate algorithm
n_folds = 5
l_rate = 0.01
n_epoch = 50
scores = evaluate_algorithm(dataset, linear_regression_sgd, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean RMSE: %.3f' % (sum(scores)/float(len(scores))))
