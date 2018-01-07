object ArrayForEachExample_Nov_10{
	def main(args: Array[String]): Unit = {
	  println("ArrayForEachExample_Nov_10")


	  var a1=Array(45,7,81,24,7777)

	  // for( i <- 0 until (a1.length)) {
	  // 		println(a1(i))
	  // }

	  a1.foreach((get:Int)=>(println(get)))

	}
	
}