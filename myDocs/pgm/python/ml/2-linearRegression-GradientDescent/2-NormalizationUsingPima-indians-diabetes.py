from csv import reader

# Load a CSV file
def load_csv(filename):
	file = open(filename, "rb")
	lines = reader(file)
	dataset = list(lines)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# Rescale dataset columns to the range 0-1
def normalize(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Load pima-indians-diabetes dataset
#filename = '/home/manohar/Downloads/winequality-white.csv'
filename = 'pima-indians-diabetes.csv'

dataset = load_csv(filename)
#print "data=",dataset[0]
print('Loaded data file {0} with {1} rows and {2} columns').format(filename, len(dataset), len(dataset[0]))
# convert string columns to float
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
print("dataset[0]=",dataset[0])
# Calculate min and max for each column
minmax = dataset_minmax(dataset)

print "minmax=",minmax
# Normalize columns
normalize(dataset, minmax)
#print(dataset[0])

#print dataset

