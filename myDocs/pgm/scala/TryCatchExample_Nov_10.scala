object TryCatchExample_Nov_10
{
	def main(args: Array[String]): Unit = {
	  println("TryCatchExample_Nov_10")


	  try { 
	    // ...
	    var a=10/0
	  } catch {
	    case exe:Exception => println(exe)
	  }
	  finally{
	  	println("asdsaddaasd")
	  }

println("rest of the code..")

}	
}