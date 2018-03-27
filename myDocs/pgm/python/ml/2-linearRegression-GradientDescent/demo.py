# Linear Regression With Stochastic Gradient Descent for Wine Quality
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
		#	print "row=",row
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):  # (whole dataset  , 0)
	for row in dataset:  #taking first row   ['7', '0.27', '0.36', '20.7', '0.045', '45', '170', '1.001', '3', '0.45', '8.8', '6']
		row[column] = float(row[column].strip())  # take out '7' from given and covert into float list [7.0,6.3,..]
		# print "row[column]=",row[column]
		# print "--------------"


# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	print "len=dataset[0]",len(dataset[0])

	for i in range(len(dataset[0])): # ['7', '0.27', '0.36', '20.7', '0.045', '45', '170', '1.001', '3', '0.45', '8.8', '6']
		# print dataset[i]
		col_values = [row[i] for row in dataset] # taking first row ['7', '0.27', '0.36', '20.7', '0.045', '45', '170', '1.001', '3', '0.45', '8.8', '6']
	        #print col_values      # print [7.0]
		value_min = min(col_values)  
		value_max = max(col_values)
		#print "min,=",value_min,value_max
		minmax.append([value_min, value_max])
	return minmax



# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0]) # [7]-
			#print "row normal=",row[i] 
	#row[0] = (row[0] - minmax[0][0]) / (minmax[0][1] - minmax[0][0]) # [7]-
			#print "row[0]=",row[i],minmax[i][0],minmax[i][1],minmax[i][0]




# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split





# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		rmse = rmse_metric(actual, predicted)
		scores.append(rmse)
	return scores




# Linear Regression on wine quality dataset
seed(1)
# load and prepare data
filename = '/home/manohar/Downloads/winequality-white.csv'
dataset = load_csv(filename)

print "len",len(dataset)
#print "dataset[o]=",dataset[0]
for i in range(len(dataset[0])):    #dataset[o]= ['7', '0.27', '0.36', '20.7', '0.045', '45', '170', '1.001', '3', '0.45', '8.8', '6']
	str_column_to_float(dataset, i)  # (whole dataset  , 0)

# normalize
minmax = dataset_minmax(dataset)
print "minmax=",minmax
normalize_dataset(dataset, minmax)


# evaluate algorithm
n_folds = 5
l_rate = 0.01
n_epoch = 50
scores = evaluate_algorithm(dataset, linear_regression_sgd, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean RMSE: %.3f' % (sum(scores)/float(len(scores))))



