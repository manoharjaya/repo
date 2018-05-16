from random import seed
from random import randrange

# zero rule algorithm for classification
def zero_rule_algorithm_classification(train, test):
	output_values = [row[-1] for row in train]
	print 'output=',output_values
	print "set=",set(output_values)
	prediction = max(set(output_values), key=output_values.count)

	'''
The function makes use of the max() function with the key attribute, which is a little clever.
Given a list of class values observed in the training data, the max() function takes a set of unique class values and calls the count on the list of class values for each class value in the set.
The result is that it returns the class value that has the highest count of observed values in the list of class values observed in the training dataset.
If all class values have the same count, then we will choose the first class value observed in the dataset.
	'''
	print "prediction-",prediction
	predicted = [prediction for i in range(len(train))]
	return predicted

seed(1)
train = [['0'], ['0'], ['0'], ['0'], ['1'], ['1']]
test = [[None], [None], [None], [None]]
predictions = zero_rule_algorithm_classification(train, test)
print(predictions)
