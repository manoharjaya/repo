from random import seed
from random import randrange

# Split a dataset into k folds
def cross_validation_split(dataset, folds=3):

	dataset_split = list()
	dataset_copy = list(dataset)
	print "dataset_copy=",dataset_copy
	fold_size = int(len(dataset) / folds)
	print "fold_size=",fold_size   # 2
	for i in range(folds):  # 4

		fold = list()  # every time new list is created 
		while len(fold) < fold_size:   # 0 < 2 
			index = randrange(len(dataset_copy))   # 10 
			fold.append(dataset_copy.pop(index))  # fold=[[],[]]
		dataset_split.append(fold) # dataset_split=[[[],[]]]
	return dataset_split

# test cross validation split
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
folds = cross_validation_split(dataset, 4)
print(folds)
