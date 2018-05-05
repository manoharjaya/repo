# demonstrates the numpy pseudorandom number generator
from numpy.random import seed
from numpy.random import rand
# seed the generator
seed(7)
print(rand(5))
# seed the generator to get the same sequence
print('Reseeded')
seed(7)
print(rand(5))
