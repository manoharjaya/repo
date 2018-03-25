object testSwitch_Dec_2
{
	def main(abc:Array[String]):Unit={
		println("testSwitch_Dec_2..")
		check("practice")
	}

	def check(temp:Any):Any=
	{
		temp match {
			case 1 =>  println(s"one=$temp")
			case "manohar" => println(s" you have to learn data structure.. $temp")
			case "practice" => println(s" $temp for data structure very hard ")
			case _ => println(s" other than your data..")
		}
		
	}
}