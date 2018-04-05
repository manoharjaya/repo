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

		# print "csv_reader=",csv_reader
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
def normalize_dataset(dataset, minmax):  #  minmax= [[3.8, 14.2], [0.08, 1.1], [0.0, 1.66], [0.6, 65.8], [0.009, 0.346], [2.0, 289.0], [9.0, 440.0], [0.98711, 1.03898], [2.72, 3.82], [0.22, 1.08], [8.0, 14.2], [3.0, 9.0]]
	for row in dataset:   
		for i in range(len(row)):    #len([7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8,6])=12
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])  # ((7.0-3.8)/(14.2-3.8))  => 0.307 , 0.186




# Linear Regression on wine quality dataset
seed(1)
# load and prepare data
# filename = '/home/manohar/Downloads/winequality-white.csv'
filename = '/home/manohar/resource/dataset/winequality-white.csv'

dataset = load_csv(filename)
# print dataset[0]

for i in range(len(dataset[0])):   # len([7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8,6]) => range(12)
	str_column_to_float(dataset, i) # (dataset,0)
# print dataset[0]

minmax = dataset_minmax(dataset)
# print "minmax=",minmax

normalize_dataset(dataset, minmax)
# print "normalize_dataset=",dataset[0]


# evaluate algorithm
n_folds = 5
l_rate = 0.01
n_epoch = 50
scores = evaluate_algorithm(dataset, linear_regression_sgd, n_folds, l_rate, n_epoch)

