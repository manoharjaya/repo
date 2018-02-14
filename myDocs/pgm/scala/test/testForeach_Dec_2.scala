object testForeach_Dec_2
{
	def main(e:Array[String]):Unit={
		println("testForeach_Dec_2..");

		var a1=Array(1,2,3,5,7)

		a1.foreach((getEach:Int)=>println(getEach))

		var a2:Array[String]=new Array[String](4)

		try { 
		  
		  	a2(0)="manohar"
			a2(1)="you"
			a2(2)="learn"
			a2(3)="data"
			a2(4)="structure"
			a2.foreach((getEach:String)=>println(getEach))

		} 
		catch {

		  case e: Exception => e.printStackTrace()

		}

		


	}
}