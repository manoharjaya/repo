object Named_Para_Nov_10
{
	def main(args: Array[String]): Unit = {
	  
	  println("Named_Para_Nov_10")

	  var res=display(a=1000,b=250)
	  println(res)
	}

	def display(a:Int,b:Int):Any = {
		println("display method is called..")
		a+b
	}
	
}