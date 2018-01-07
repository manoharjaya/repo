object singleTon_Nov_10{
	def display():Unit=
	{
		println("test display..");
	}
	def main(args: Array[String]): Unit = {
	display()
	 println("singleTon_Nov_10\n"+singleTon.single_display(50,20))
	}
	
}

object singleTon{
	def single_display(a:Int,b:Int):Int={
		a+b
	}
}
