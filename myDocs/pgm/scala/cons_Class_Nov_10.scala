object cons_Class_Nov_10
{
	def main(args: Array[String]): Unit = {
	  println("cons_Class_Nov_10")


	  val s1=new Student("manohar",22,"Data Structure")
	  s1.display()
	}
	
}


class Student(name:String,age:Int){

	def this(name:String,age:Int,designation:String)
	{
		this(name:String,age:Int)
		println("auxilary cons with 3 parameter..")
		println(designation)
		

	}
	def display():Unit = {
		println("name="+name+"\t"+"age="+age)
	}

}