object ArrayFuncExample_Nov_10{
	def main(args: Array[String]): Unit = {
	  println("ArrayFuncExample_Nov_10")

	  val a1=Array(45,5,8,4,770)
	  for(i<- 0 until (a1.length))
	  	println(a1(i))
	  println(getArray(a1))

	}


	def getArray(arr:Array[Int]):Int = {
		var sum=0
		for(i<- 0 until (arr.length))
	  	sum=sum+arr(i)
	  	sum
	}
	
}