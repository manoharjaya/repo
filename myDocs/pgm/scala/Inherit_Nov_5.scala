class parent(val name:String,val age:Int,var occupation:String) {
	val Name:String=name
	val Age:Int=age
	val Occupation:String=occupation

	def parent_display():Unit={
		println("Hello parent="+Name)
	}
}



object Inherit_Nov_5
{
	def main(args: Array[String]): Unit = {

	  println("Inherit_Nov_5.."+display())

	  val p1=new parent("Manohar",22,"data scientist")

	  println("Name="+p1.Name+",Age="+p1.Age+",Occupation="+p1.Occupation)

	  p1.parent_display()

	  


	}
	def display():String={
		var name:String="Manohar"
		name
	}
	
}