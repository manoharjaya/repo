import scala.collection.mutable.ArrayBuffer
import scala.math.Ordering
class Student(name:String,age:Int,occu:String)
{
	// def display():Unit={
	// 	println("name="+name+",age="+age+",occu="+occu)   // return as Unit
	// }

	override def toString(): String =  
	{
		s"Name=$name\tAge=$age\tOccu=$occu"   // s returns String Interpolations to the calling functions
	} 
	
}
object listOfStudent
{
	def main(args: Array[String]): Unit = {
	  println("listOfStudent")

	  var s1=new Student("manohar",23,"java developer");
	  var s2=new Student("ram",25,"video grapher");
	  var s3=new Student("Lakshman",25,"Image Editor");
	  var s4=new Student("jaya",40,"Home");
	  
	  println(s1)

	  println
	  var arrbuf=new ArrayBuffer[Student]

	  // arrbuf+=s1;
	  // arrbuf+=s2;
	  // arrbuf+=s3;
	  // arrbuf+=s4;

	  	// Either or

		arrbuf+=(s1,s2,s3,s4)

	  for(i<-arrbuf) 
	  	println(i)

	  val sortedDudes = s1.sortWith(_.name < _.name)
	  println(sortedDudes)
	  // s1.display();
	}
	
}