import java.sql.*;

class HiveCreateDb
{
	private static String driverName = "org.apache.hadoop.hive.jdbc.HiveDriver";
   
	public static void main(String[] args) {
		
		try
		{
			Class.forName(driverName);
			Connection conn=DriverManager.getConnection("jdbc:hive//localhost:10000/default","","");

			Statement stat=conn.createStatement();

			stat.executeQuery("CREATE DATABASE javadb");

			System.out.println("DATABASE created sucessfully..");

			conn.close();
		}
		catch (Exception e) {
			System.out.println(e);
		}

	}
}
