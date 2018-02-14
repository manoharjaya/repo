import scala.util.control.Breaks._
object For_Nov_10
{
	def main(dsada:Array[String]):Unit={
		println("For_Nov_10..")
// -------------general------------------
		for(a <- 1 to 10)
			println(a)
// ---------------until------------------
		for( a <- 1 until 10) 
			println(a)
// ---------------filtering------------------
		for( a <- 0 to 10 if a%2==0)
			println(a)
// -------------yield------------------
		var result=for( a <- 10 to 20) yield a 
			for(i <- result if i%2==0)
				println("i="+i)
// ---------------Itreating------------------
		var l1=List(25,75,7,2,54,98)
		for(i<-l1) 
			println(i)

		println 
		println 
		println("mano")
							// foreach block
		l1.foreach{
			println
		}
		println
							// foreach function
		l1.foreach(print)
		println
		l1.foreach((ele:Int)=>print(ele))     // foreach  assignment


		for( i <- 1 to 10 by 2 ) {
				if(i==7)
				break
				println(i)

		}

	}


}