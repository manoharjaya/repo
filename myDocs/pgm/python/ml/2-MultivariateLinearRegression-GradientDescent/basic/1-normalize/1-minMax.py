# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):  #2
		col_values = [row[i] for row in dataset] #          [50]   <= [50,30]  , [50,20]  <= [20, 90]
		value_min = min(col_values) # 20
		value_max = max(col_values) # 50 
		minmax.append([value_min, value_max])  #[20,50]
	return minmax

# Contrive small dataset
dataset = [[50, 30], [20, 90]]
print(dataset) 
# Calculate min and max for each column
minmax = dataset_minmax(dataset)
print(minmax)
