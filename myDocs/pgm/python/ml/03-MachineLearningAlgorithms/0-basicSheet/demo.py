from csv import reader

# from random import seed
# from random import randrange

# Simple Linear Regression on the Swedish Insurance Dataset



from random import randrange

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			dataset.append(row)
	return dataset


dataset = load_csv("/home/manohar/resource/dataset/insurance.csv")

print "l=",0.6*len(dataset)

print len(dataset)

index = randrange(len(dataset)) 


# Convert string column to float
def str_column_to_float(dataset, column):
	print "helo"
	for row in dataset:
		print "row",row
		if (row[column]=='X' or row[column]=='Y'):
			continue
		row[column] = float(row[column].strip())
		# print "column=%d"%(column),row[column]

 

for i in range(len(dataset[0])):
	# print "i :",i
	str_column_to_float(dataset,i)


print "index=",index
# print len(dataset[0]), dataset
print "pop=",dataset.pop(index)


train = list()
print len(train)



def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:   # 0 < 38.4
		index = randrange(len(dataset_copy))     #  it gives the random range  
		train.append(dataset_copy.pop(index))   # popout the element on that index and append it on train
	return train, dataset_copy


dataset = load_csv("/home/manohar/resource/dataset/insurance.csv")


train, test = train_test_split(dataset, 0.6)

print "-------------------------------------------"

print "train  ",len(train)

print "-------------------------------------------"

print "test " ,len(test)











# Simple Linear Regression on the Swedish Insurance Dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		print "row",row
		if (row[column]=='X' or row[column]=='Y'):
			continue
		row[column] = float(row[column].strip())

# Split a dataset into a train and test set
def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy

# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, split, *args):
	train, test = train_test_split(dataset, split)
	test_set = list()
	for row in test:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(train, test_set, *args)
	actual = [row[-1] for row in test]
	rmse = rmse_metric(actual, predicted)
	return rmse

# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

# Simple linear regression algorithm
def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return predictions

# Simple linear regression on insurance dataset
seed(1)
# load and prepare data
filename = '/home/manohar/resource/dataset/insurance.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
# evaluate algorithm
split = 0.6
rmse = evaluate_algorithm(dataset, simple_linear_regression, split)
print('RMSE: %.3f' % (rmse))





filename = '/home/manohar/resource/dataset/a.csv'
dataset = load_csv(filename)

total=0.0
con=list()
for row in dataset:
	print "sss=",row[0]
	# if row[0]=='X' or row[0]=='Y':
	# 	continue
	# con.append(row[0])


	# print "float=",float(row[0])
print "con",con
print total






