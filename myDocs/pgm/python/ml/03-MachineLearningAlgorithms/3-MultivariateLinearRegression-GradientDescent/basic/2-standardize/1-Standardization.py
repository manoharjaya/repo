from math import sqrt

# calculate column means
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]  # means =[0,0]
	print 'means=',means
	for i in range(len(dataset[0])): 
		col_values = [row[i] for row in dataset] # col_values = [50,20,30] 
		means[i] = sum(col_values) / float(len(dataset)) #  33.33
	return means

# calculate column standard deviations
def column_stdevs(dataset, means):   #    [50, 30], [20, 90], [30, 50] ,[33.333333333333336, 56.666666666666664]
	stdevs = [0 for i in range(len(dataset[0]))]   # stdevs = [0,0] 
	for i in range(len(dataset[0])):  # 2 
		variance = [pow(row[i]-means[i], 2) for row in dataset]  # var=[277.88,177.688,11.08],[710.755,1111.55,44.35]
		stdevs[i] = sum(variance)  # stdevs = [466.6479,1866.654]
	stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs] #  stdevs=[15.27494,30.55040]
	return stdevs


# standardize dataset  z rule using statistics 
def standardize_dataset(dataset, means, stdevs):    # z= x- meanx/std
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - means[i]) / stdevs[i]  # row=[[1.07,-0.8],[]]



# Standardize dataset
dataset = [[50, 30], [20, 90], [30, 50]]
print(dataset)
# Estimate mean and standard deviation
means = column_means(dataset)
stdevs = column_stdevs(dataset, means)
print(means)
print(stdevs)

# standardize dataset
standardize_dataset(dataset, means, stdevs)
print(dataset)


