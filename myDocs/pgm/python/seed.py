import random



print random.random()

random.seed(12)  # once you set the seed(12) no it will not set after again invoke random.random() function
 
print
for x in xrange(0,10):
	print x,random.random()
