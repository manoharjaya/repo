from random import seed
from random import randrange

# Generate random predictions
def random_algorithm(train, test):
	output_values = [row[-1] for row in train]
	#print "output_values=",(output_values)
	print "output_values=",set(output_values)
	print "output_values=",list(set(output_values))
	unique = list(set(output_values))
	predicted = list()
	for row in test:
		index = randrange(len(unique))
		#print "index=",index
		predicted.append(unique[index])
	return predicted

seed(1)
train = [[0], [1], [0], [1], [0], [1]]
test = [[None], [None], [None], [None]]
predictions = random_algorithm(train, test)
print(predictions)
