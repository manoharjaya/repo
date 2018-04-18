# Find the min and max values for each column
def dataset_minmax(dataset):
        minmax = list()
        for i in range(len(dataset[0])):  #2
                col_values = [row[i] for row in dataset] #          [50]   <= [50,30]  , [50,20]  <= [20, 90]
                value_min = min(col_values) # 20
                value_max = max(col_values) # 50 
                minmax.append([value_min, value_max])  #[20,50]
        return minmax


# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):  #  [[50, 30], [20, 90]], [[20,50],[30,90]  
	for row in dataset:  #  [[50, 30], [20, 90]]
		for i in range(len(row)): #  [50, 30]
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])    # (50-20)/(50-20)  
			# row[i]=[[1,0],[0,1]]

# Contrive small dataset
dataset = [[50, 30], [20, 90]]
print(dataset)
# Calculate min and max for each column
minmax = dataset_minmax(dataset)
print(minmax)
# Normalize columns
normalize_dataset(dataset, minmax)
print(dataset)
