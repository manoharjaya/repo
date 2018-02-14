object testDowhile_Dec_2
{
	def main(asdf:Array[String]):Unit={
		println("DoWhile_Dec_2..")
		var test:Int=0
		var sum:Int=0
		do
		{
			test=test+1;
			sum=sum+test;
		}
		while(test!=5)
		println(sum)
	}
}