import scala.collection.mutable.ArrayBuffer
object ArrayBuffer_Nov_12
{
	def main(args: Array[String]): Unit = {
	  println("ArrayBuffer_Nov_12")
	  var arrbuf=new ArrayBuffer[Int](5);
	  var arr=Array(1,2,3,4,5,6,7,8,9,10)
	  arrbuf+=10
	 arrbuf+=(2,5,7,77)

	 println(arrbuf)
	 println
	 println(arr) // note
	 for( i <- 0  until (arr.length)) {
	 	println(arr(i))
	 }
	var add=arrbuf++arr
	println(add)
	}
	
}