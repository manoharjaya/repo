object ArrayExample{
	def main(args: Array[String]): Unit = {
	  println("ArrayExample")


	  var a1=Array(12,54,8,7,9,78)
	  for( i <- 0 until (a1.length)) {
	  		println(a1(i))
	  }

println
	  var a2:Array[Int]=new Array[Int](5)

	  a2(2)=77
	   for( i <- 0 until (a2.length)) {
	  		println(a2(i))
	  }

	}
	
}



