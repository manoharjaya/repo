import scala.collection.mutable.ArrayBuffer
object testArrayBuffer_Dec_2
{
	def main(asd:Array[String]):Unit={
		println("testArrayBuffer_Dec_2")
		var a:ArrayBuffer[Int]=new ArrayBuffer[Int](5)
		// var a=new ArrayBuffer[Int](5);
		a +=100;
		a +=150
		a +=200
		
		a.foreach{
			println
		}
	}
}