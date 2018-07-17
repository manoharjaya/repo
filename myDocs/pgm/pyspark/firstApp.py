from pyspark import SparkContext

logFile='readme.md'
sc=SparkContext('local','myFirstpysparkApp')
logData=sc.textFile(logFile).cache()
#logData=sc.textFile(logFile).count()
numAs=logData.filter(lambda s : 'a' in s).count()
numBs=logData.filter(lambda s : 'b' in s).count()
print 'Num of As=%d and Bs=%d'%(numAs,numBs)


