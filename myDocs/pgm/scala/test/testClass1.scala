object testClass1
{
	def main(asdf:Array[String]):Unit={
		println("testClass1")
		val s1=new Student(0,"")
		println(s1.id+" "+s1.name)
		println
		val s2=new Student(1173,"manohar learn data structure..")
 		println(s2.displayRecord())
 	}
}

class Student(val pid:Int,val pname:String)
{
	var id:Int=0;
	var name:String=null;
	def displayRecord():Any={
		pid+" "+pname
	}
	
}