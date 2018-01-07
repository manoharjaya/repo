object testArray_Dec_2
{
	def main(asdf:Array[String]):Unit={
		println("ArrayExample_Nov_10")

		var a1=Array(12,2,54,8,7)
		displayArray(a1)

		var a2:Array[Int]=new Array[Int](5)
		a2(2)=10000;
		a2(4)=50000;
		displayArray(a2)
	}

	def displayArray(tempArr:Array[Int]):Any={
		// for(i <- 0 until tempArr.length)
		// 	println(tempArr(i))
		// for(i <- tempArr)
		// 	println(i)
		for( i <- 0 to (tempArr.length)-1) {
			println(tempArr(i))
		}
	}
}