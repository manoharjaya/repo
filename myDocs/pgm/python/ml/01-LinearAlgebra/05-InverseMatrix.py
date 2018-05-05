# invert matrix
from numpy import array
from numpy.linalg import inv
# define matrix
A = array([[1.0, 2.0], [3.0, 4.0]])
print(A)
# invert matrix
B = inv(A)  #In other words: swap the positions of a and d, put negatives in front of b and c, and divide everything by the determinant (ad-bc).
print(B)

