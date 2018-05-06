// Java program to demonstrate syntax of assertion
import java.util.Scanner;

class Test
{
	public static void main( String args[] )
	{
		int value = 15;
		assert value >= 20 : " Underweight";
		System.out.println("value is "+value);
	}
}


/**
By default, assertions are disabled. We need to run the code as given. The syntax for enabling assertion statement in Java source code is:

java –ea Test

Disabling Assertions

The syntax for disabling assertions in java are:

java –da Test
*/