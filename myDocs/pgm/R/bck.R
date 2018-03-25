print(10+20)
print hello
print "hello"
print ("hello manohar R")
print ("Hello manohar")
print("hello manohar")
print(12.5+12.5)
print(12.5+12.5)
print("hello manohar")
myString <- "hello mystring"
print(myString)
print ("hello manohar")
print(22+15)
if(TRUE)
{
"HELLO manohar"
}
mystr <- "hello outside if"
print(mystr)
"without print functions"
v  <- TRUE
print(class(v))
v  <- 10
print(class(v))
v  <- 10.5
print(class(v))
v  <- "mano"
print(class(v))
v  <- 10L
print(class(v))
v  <- 10+5i
print(class(v))
v  <- 10+5i
v <- charToRaw("mano")
print(class(v))
vec <- c("red","green","blue")
print(class(vec))
"A list is an R-object which can contain many different types of elements inside it like vectors, functions and even another list inside it."
"# Create a list.
"
list1 <- list(c(2,5,3),21.3,sin)
print(class(list1))
print(list1)
savehistory("~/pgm/R/bck.R")
print(list1)
# Create a matrix
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
print(M)
M = matrix( c("manohar","jaya","ram","lakshman","ravi","shekhar"), nrow = 2, ncol = 3, byrow = TRUE)
print(M)
# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')
# Create a factor object.
factor_apple <- factor(apple_colors)
# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))
# Create the data frame.
BMI <- 	data.frame(
gender = c("Male", "Male","Female"),
height = c(152, 171.5, 165),
weight = c(81,93, 78),
Age = c(42,38,26)
)
print(BMI)
var1 = c(1,2,3,4,5)
var1
var_x <- "Hello"
cat("The class of var_x is ",class(var_x),"\n")
var_x <- 34.5
cat("  Now the class of var_x is ",class(var_x),"\n")
var_x <- 27L
cat("   Next the class of var_x becomes ",class(var_x),"\n")
print(ls())
print(ls(pattern = "my"))
print(ls(pattern = "var"))
print(ls(pattern = "v"))
print(ls(all.names = TRUE))
rm(var1)
print(var1)
print(var)
rm (list=ls())
print(ls())
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v+t)
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v-t)
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v*t)
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v/t)
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v%%t)
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v>t)
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v < t)
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v == t)
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v<=t)
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v>=t)
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v!=t)
x <- 10
if(is.integer(x))
{}
if(is.integer(x)){}
if(is.integer(x)){}
if(is.integer(x)){"hello",x}
if(is.integer(x)){"hello"+x}
x <- 10
if(is.integer(x)){}
if(is.integer(x)){print("hello integer")}
if(is.integer(x)){print("hello integer")}
# Create a sequence of numbers from 32 to 44.
print(seq(32,44))
print(mean(25:82))
print(sum(1:5))
data <- read.csv("input.csv")
print(data)
data <- read.csv("/home/manohar/resource/dataset/company.csv")
print(data)
data <- read.csv("/home/manohar/resource/dataset/baby_names.csv")
print(data)
maxCount <- max(data$Count)
print(maxCount)
retval <- subset( data, dept == "MORGAN")
print(retval)
retval <- subset( data, First.Name == "MORGAN")
print(retval)
retval <- subset( data, First.Name == "MORGAN")
print(retval)
savehistory("~/pgm/R/bck.R")
me<- 1:5
print(me)
me <- seq()
me <- seq(1:5)
print(me)
me <- c(1,2,3,4,5)
print(me)
val1 <- c(1,2,3,4,5)
me<- mean(val1)
print(me)
med<-median(val1)
print(med)
median.result=median(val1)
print(median.result)
val1 <- c(1,2,3,4,5,6)
print(median.result)
median.result=median(val1)
print(median.result)
print(median.result)
var1<-c(1,2,3,4,5)
var2<-c(1,2,3,4,5)
relation <- lm(var2~var1)
print(relation)
Sys.setenv(HADOOP_CMD="/home/manohar/hadoop/bin/hadoop");
Sys.setenv(HADOOP_STREAMING="/home/manohar/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar");
install.packages("rmr2")
library(rmr2)
Sys.setenv(HADOOP_CMD="/home/manohar/hadoop/bin/hadoop");
Sys.setenv(HADOOP_STREAMING="/home/manohar/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar");
install.packages("rmr2")
install.packages("rmr2")
library(rmr2)
library(rhdfs)
library(rhdfs)
hdfs.init()
savehistory("~/pgm/R/bck.R")
Sys.setenv(HADOOP_CMD="/home/manohar/hadoop/bin/hadoop");
Sys.setenv(HADOOP_STREAMING="/home/manohar/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar");
library(rmr2)
library(rhdfs)
hdfs.init()
hdfs.mkdir("/output/")
hdfs.ls("/output")
?mapreduce
map_func<- function(key,lines)
{
listofwords<-strsplit(lines,"\\s+")
words<-unlist(listofwords)
return(words,1)
}
reduce_func<- function(mapoutput,tuple)
{
return(mapoutput,sum(tuple))
}
wordcount<- function(input,output=NULL)
{
mapreduce(input=input,output=output,input.format = "text",map=map_func,reduce = reduce_func)
}
hdfs.ls("\input\")
hdfs.ls("/input/")
Sys.setenv(HADOOP_CMD="/home/manohar/hadoop/bin/hadoop");
Sys.setenv(HADOOP_STREAMING="/home/manohar/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar");
library(rmr2)
library(rhdfs)
hdfs.init()
basedir<- "/input/"
inputFile<- file.path(basedir,"Input.txt")
outputFile<-file.path("/output/","R_MapReduce_wordcount_output_feb14")
wordcount<- function(input,output=NULL)
{
mapreduce(input=input,output=output,input.format = "text",map=map_func,reduce = reduce_func)
}
wordcount(inputFile,outputFile)
hdfs.cat("/output/R_MapReduce_wordcount_output_feb14")
hdfs.ls("/output/R_MapReduce_wordcount_output_feb14")
hdfs.cat("/output/R_MapReduce_wordcount_output_feb14/part-00000")
result<-from.dfs(outputFile)
result.df=data.frame(result,stringsAsFactors = F)
colnames(result.df)<-c("word","count")
colnames(result.df)<-c("word")
colnames(result.df)<-c('word','count')
result.df
result<-from.dfs(outputFile)
result.df=as.data.frame(result,stringsAsFactors = F)
colnames(result.df)<-c('word','count')
result.df
result<-from.dfs(outputFile)
View(result)
result.df=as.data.frame(result,stringsAsFactors=F)
View(result.df)
colnames(result.df)<-c('word','count')
result.df
Sys.setenv(HADOOP_CMD="/home/manohar/hadoop/bin/hadoop");
Sys.setenv(HADOOP_STREAMING="/home/manohar/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar");
hdfs.init()
result<-from.dfs(outputFile)
result.df=as.data.frame(result,stringsAsFactors=F)
result.df
colnames(result.df)<-c('word','count')
print(result)
results.df=as.data.frame(result,stringsAsFactors=F)
results.df
result<-from.dfs(outputFile)
results.df=as.data.frame(result,stringsAsFactors=F)
colnames(results.df)<-c('word','count')
results.df
print(results.df)
map_func<- funtion(key,lines)
{
listofwords<-strsplit(lines,"\\s+")
words<-unlist(listofwords)
return(words,1)
}
reduce_func<- function(mapoutput,tuple)
{
return(mapoutput,sum(tuple))
}
wordcount<- function(input,output=NULL)
{
mapreduce(input=input,output=output,input.format = "text",map=map_func,reduce = reduce_func)
}
basedir<- "/input/"
inputFile<- file.path(basedir,"Input.txt")
outputFile<-file.path("/output/","R_MapReduce_wordcount_output_feb14")
ret<-wordcount(inputFile,outputFile)
basedir<- "/input/"
inputFile<- file.path(basedir,"Input.txt")
outputFile<-file.path("/output/","R_MapReduce_wordcount_output_feb14")
ret<-wordcount(inputFile,outputFile)
result<-from.dfs(outputFile)
View(result)
results.df=as.data.frame(result,stringsAsFactors=F)
colnames(results.df)<-c('word','count')
results.df<-as.data.frame(result,stringsAsFactors=F)
colnames(results.df)<-c('word','count')
result<-from.dfs(outputFile)
results.df<-as.data.frame(result,stringsAsFactors=F)
View(results.df)
View(results.df)
View(retval)
View(result.df)
View(results.df)
colnames(results.df)<-c('word','count')
result<-from.dfs(outputFile)
data.df<-as.data.frame(result,stringsAsFactors=F)
View(data)
colnames(data.df)<-c('word','count')
colnames(data.df)<-c('word')
result<-from.dfs(outputFile)
results.df<-as.data.frame(result,stringsAsFactors=F)
colnames(results.df)<-c('word','count')
results.df
result<-from.dfs(ret)
View(result)
result<-from.dfs("/output/R_MapReduce_wordcount_output_feb14/part-00000")
View(result)
results.df<-as.data.frame(result,stringsAsFactors=F)
colnames(results.df)<-c('word','count')
savehistory("~/pgm/R/bck.R")
