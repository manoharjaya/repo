object default_Func_Nov_10
{
	def  main(args: Array[String]): Unit = {
	  
		var result=display(10);

		var result1=display(100);
		var result2=display(1000,1523);
		println(result+""+result1+""+result2	)

		

	}
	def display(a:Int=0,b:Int=0):Any = {
			println("Hello default_Func_Nov_10..")
			a+b
	}
	
}