from numpy import array
from numpy import var
v = array([1,2,3,4,5,6])
print(v)
result = var(v, ddof=1) #sample variance
print("sample variance=",result)

result = var(v) #population variance
print("population  variance=",result)


M = array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(M)
col_mean = var(M, ddof=1, axis=0)
print(col_mean)
row_mean = var(M, ddof=1, axis=1)
print(row_mean)
