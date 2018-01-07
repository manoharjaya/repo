import org.apache.spark.SparkConf;
import org.apache.spark.SparkContext;

object WordCount 
{
   def main(args: Array[String]) {

     //Create conf object
     val conf = new SparkConf().setAppName("WordCount")//.setMaster("local")

     //SparkSession spark = SparkSession.builder().appName("SomeAppName").config("spark.master", "local").getOrCreate();

     //create spark context object
     val sc = new SparkContext(conf)

     if (args.length < 2) {
     	println("Usage: ScalaWordCount <input> <output>")
	     System.exit(1)
     }

     //Read file and create RDD
     val rdd1 = sc.textFile(args(0))
     //convert the lines into words using flatMap operation

     val rdd2 = rdd1.flatMap(line => line.split(" "))
     //count the individual words using map and reduceByKey operation
    
     val rdd3 = rdd2.map(word => (word, 1)).reduceByKey(_ + _)

     //Save the result
     rdd3.saveAsTextFile(args(1))

    //stop the spark context
     sc.stop
 }
}