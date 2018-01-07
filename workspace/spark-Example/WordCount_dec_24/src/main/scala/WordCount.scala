import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
 
object WordCount 
{
 def main(args: Array[String]) 
 {
	 val logFile = "/home/manohar/resource/dataset/Input.txt"
	 val sparkConf = new SparkConf().setAppName("Spark Word Count")
	 val sc = new SparkContext(sparkConf)
	 val file = sc.textFile(logFile)
	 val counts = file.flatMap(_.split(" ")).map(word => (word, 1)).reduceByKey(_ + _) 
	 counts.saveAsTextFile("/home/manohar/resource/output/spark/WordCount_out_dec_24")
 }
}