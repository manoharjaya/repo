object Array_Nov_5
{
	def main(args: Array[String]): Unit = {
	
	  println("Hello")

	  var a_variable:Array[Int]=Array(75,55,78,7410)
	  var index:Int=0
	  // for(  index<- 0 to (a_variable.length)-1) {
	  // 		println("a_variable="+a_variable(index))
	  // }
	  // for(  index<- 0 until a_variable.length) {
	  // 		println("a_variable="+a_variable(index))
	  // }
	  for(  index<- a_variable) {
	  		println("a_variable="+index)
	  }

	}

}