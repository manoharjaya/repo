from numpy import array
import numpy.matlib
a = array([[1,2],[3,4]])   # A matrix is a two-dimensional array of scalars with one or more columns and one or more rows
b = array([[11,12],[13,14]]) 

print "a=", a
print
print "b=",b
print "\nmatrix addition"
c=a+b
print "c=",c
print "\nmatrix subtraction"
c=a-b
print "c=",c
c=numpy.dot(a,b)
print
print "c=",c

print
# matrix dot product
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
B = array([[1, 2], [3, 4]])
print(B)
C = A.dot(B)
print(C)