object anonymousObj_Dec_2 {
	def main(ar:Array[String]):Unit=
	{
		println("hello test..")
		println("anonymousObj is called .."+display)
	}
	def display():Unit=
	{
		println("welcome display")
		println(new test().display2(50))
	}
}


class test {
	def display2(a: Int):Int = {
		return (25+a)
	}
}
