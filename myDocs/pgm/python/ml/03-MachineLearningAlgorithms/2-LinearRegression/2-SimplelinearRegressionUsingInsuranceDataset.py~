'''
x=[1,2,4,3,5]
y=[1,3,3,2,5]



mean=lambda l: sum(l)/float(len(l))
mx,my=mean(x),mean(y)
print "mx=%.1f and my=%.1f" %(mx,my)



variance=lambda l,ml: sum([(x-ml)**2 for x in l])
varx,vary=variance(x,mx),variance(y,my)
print "varx=%.1f and vary=%.1f" %(varx,vary)



covar=0.0

covariance=lambda x,mean_x,y,mean_y:sum([(x[index]-mean_x)*(y[index]-mean_y) for index in range(len(x))])



covar=covariance(x,mx,y,my)
print "covar: %.1f"%covar

b1=covariance(x,mx,y,my)/variance(x,mx)
print "b1 :%.1f"%b1

b0=my-b1*mx
print "b0 :%.1f"%b0


print "#----------------------------------------------------------#"



#-------------------------------------------------------------#


# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values)/float(len(values))    # convert to float otherwise it discards the precision value

# Calculate the variance of a list of numbers
def variance(values,mean_x):
	return sum([(x-mean_x)**2 for x in values])

# Calculate covariance between x and y
def covariance(x,mean_x,y,mean_y):
	return sum([(x[index]-mean_x)*(y[index]-mean_y) for index in range(len(x))])




def co_efficients():

	dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
	x=[row[0] for row in dataset]
	y=[row[1] for row in dataset]

	mean_x,mean_y=mean(x),mean(y)

	varx,vary=variance(x,mean_x),variance(y,mean_y)

	covar=covariance(x,mean_x,y,mean_y)

	b1=covar/varx

	b0=mean_y-b1*mean_x                #b0=y-b1x

	return [b1,b0]
#2d list
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

# print dataset[2][0]


# for x in xrange(len(dataset)):
# 	for y in xrange(len(dataset[x])):
# 		print dataset[x][y]
# 	print " "
	


# for z in range(len(dataset)):
# 	for e in range(len(dataset[z])):
# 		print dataset[z][e]


# x=[row[0] for row in dataset]
# y=[row[1] for row in dataset]


# mean_x,mean_y=mean(x),mean(y)
# print "mean_x : %.1f mean_y : %.1f" %(mean_x,mean_y)


# varx,vary=variance(x,mean_x),variance(y,mean_y)
# print "varx : %.1f vary : %.1f" %(varx,vary)


# covar=covariance(x,mean_x,y,mean_y)

# print "covar : %.1f" %covar


# co_eff=co_efficients()

# print "co_efficients of b1 is %.1f b0 is %.1f" %(co_eff[0],co_eff[1])




'''




#----------------------------------------------------------------------------




# Standalone simple linear regression example
from math import sqrt     #math func
from csv import reader    # csv reader
from random import randrange   # gives random range 
from random import seed     # gives random range 



# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			# print "file=",row
			dataset.append(row)
	return dataset



# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		# print "row",row
		# if (row[column]=='X' or row[column]=='Y'):
		# 	continue
		row[column] = float(row[column].strip())
		# print "column=%d"%(column),row[column]


# Split a dataset into a train and test set
def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)    #  60/100=0.6 => 0.6*64 => 38.4
	dataset_copy = list(dataset)
	while len(train) < train_size:   # 0 < 38.4   60 percent of training size
		index = randrange(len(dataset_copy))     #  it gives the random range  
		train.append(dataset_copy.pop(index))    # popout the element on that index and append it on train
	return train, dataset_copy    # train data is 39 and remaining dataset_copy data is 25 ie. 60 ratio on training data




# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)


# Evaluate regression algorithm on training dataset
def evaluate_algorithm(dataset, algorithm, split, *args):   # dataset , algorithm=simple_linear_regression
	test_set = list()            # declare a list varible with empty list()
	train, test = train_test_split(dataset, split)
	for row in test:          # get each value like [1,1] from given dataset [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
		
		row_copy = list(row)     # declare a list  for ony row field like [1,1] and add [1,1],[2,3] and so on
		
		row_copy[1] = None      # assign row_copy 1 st index to be None like [1,None]
		
		test_set.append(row_copy)   # put into test_set list like [1,None],[2,None] and so on
 		
	predicted = algorithm(train, test_set, *args)# call simple_linear_regression function with (dataset , [1,None])
	print "predicted=",predicted

	actual = [row[1] for row in test]    # getting 1 st index from the dataset like [1,3,3,2,5] from  [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
	rmse = rmse_metric(actual, predicted)  #  finding average error
	return rmse



# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values)/float(len(values))    # convert to float otherwise it discards the precision value


# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# Calculate the variance of a list of numbers
def variance(values,mean_x):
	return sum([(x-mean_x)**2 for x in values])

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
	b0, b1 = coefficients(train)  # getting b1 and b0
	print "bo=%.1f\tb1=%.1f"%(float(b1),float(b0))
	for row in test:  #  ( In test list has [1,None],[2,None])
		
		yhat = b0 + b1 * float(row[0])  # getting only no like 1,2  and multiply coressponding co_eff
		predictions.append(yhat)  # it is a predicted value
	# print "len=",len(predictions)
	return predictions    # return the list







# Simple linear regression on insurance dataset
seed(1)

# load and prepare data
filename = 'dataset/insurance.csv'
dataset = load_csv(filename)
print "dataset=",dataset
for i in range(len(dataset[0])):   # ['108', '392.5']
	str_column_to_float(dataset, i)

# evaluate algorithm
split = 0.6   # split on 60 percent by size of dataset is 64 ie. 60/100=0.6 => 0.6*64 => 38.4
rmse = evaluate_algorithm(dataset, simple_linear_regression, split)
print('RMSE: %.3f' % (rmse))
