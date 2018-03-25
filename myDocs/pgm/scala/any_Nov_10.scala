object any_Nov_5
{
	def main(args: Array[String]): Unit = {
	  println("any_Nov_5")
	  switchCase("manohar")
	}

	def switchCase(test:Any):Any = {
		test match {
			case 1 => println("One search")
			case "two" => println("two search")
			case "manohar" => println("manohar you are using scala and learn data structure")
			case _ => println("nothing")

		}
		
	}
	
}