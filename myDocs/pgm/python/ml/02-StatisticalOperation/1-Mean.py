from numpy import array
from numpy import mean
v = array([1,2,3,4,5,6])
print("v=",v)
result = mean(v)
print("result=",result)

print
M = array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print("2D M=",M)
col_mean = mean(M, axis=0)
print("col_mean=",col_mean)
row_mean = mean(M, axis=1)
print("row_mean=",row_mean)
