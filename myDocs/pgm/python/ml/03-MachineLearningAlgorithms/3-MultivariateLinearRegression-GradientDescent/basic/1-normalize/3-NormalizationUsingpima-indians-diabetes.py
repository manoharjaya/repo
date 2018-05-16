from csv import reader

# Load a CSV file
def load_csv(filename):
	file = open(filename, "rb")
	lines = reader(file)
	dataset = list(lines)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):   # column = 0
	for row in dataset:   #['6','148','72',35,0,33.6,0.627,50,1],['1','85',66,29,0,26.6,0.351,31,0]
		row[column] = float(row[column].strip())  # string to float  , row[0]=[6], row[0]=[1]  for above given dataset

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset] # aggregate all column i th value into one col_values list =[1,...,,768]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Load pima-indians-diabetes dataset
filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns').format(filename, len(dataset), len(dataset[0]))
# convert string columns to float

#print("before convert=",dataset[0])

for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)

print 
print "The first record from the dataset is printed before and after normalization, showing the effect of the scaling."
print(dataset[0])
# Calculate min and max for each column
minmax = dataset_minmax(dataset)
# Normalize columns
normalize_dataset(dataset, minmax)
print(dataset[0])




