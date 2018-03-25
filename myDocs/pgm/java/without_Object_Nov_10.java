import java.util.*;
class without_Object_Nov_10  {
    
	public static void main(String[] args) {
		

	String s = "this is a test this is a test";
      String[] splitted = s.split(" ");
      Map<String, Integer> hm = new HashMap<String, Integer>();

      for (int i=0; i<splitted.length ; i++) {    //8
         if (hm.containsKey(splitted[i])) {
            int cont = hm.get(splitted[i]);
            hm.put(splitted[i], cont + 1);
         } else {
            hm.put(splitted[i], 1);
         }
      }
      System.out.println(hm);
		
	}
	public static void display()
		{
			System.out.println("Hello manohar you are testing..");
		}

}




word count using map