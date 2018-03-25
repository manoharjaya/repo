

mean=lambda x: sum(x)/float(len(x))

variance=lambda x,mean: sum([(get-mean)**2  for get in x])

covariance=lambda x,m_x,y,m_y:sum([(x[index]-m_x)*(y[index]-m_y) for index in range(len(x))])


dataset=[[1,1],[2,3],[4,3],[3,2],[5,5]]

x=[row[0] for row in dataset]
y=[row[1] for row in dataset]

print x,y



m_x,m_y=mean(x),mean(y)

v_x,v_y=variance(x,m_x),variance(y,m_y)

covar=covariance(x,m_x,y,m_y)



print "m_x=%.1f\tm_y=%.1f"%(m_x,m_y)

print "v_x=%.1f\tv_y=%.1f"%(v_x,v_y)

print "covariance=%.1f"%covar
print "len",len(range(10))