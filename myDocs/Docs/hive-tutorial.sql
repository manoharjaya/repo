



-- Before you run hive for the first time, run


schematool -initSchema -dbType derby


-- If you already ran hive and then tried to initSchema and it's failing


mv metastore_db metastore_db.tmp


-- Re run


schematool -initSchema -dbType derby


-- Run hive again




CREATE DATABASES
--------------------

CREATE DATABASE IF NOT EXISTS userdb;

		or

CREATE SCHEMA temp;



------------------------------------



import java.sql.*;


class HiveCreateDb
{
	private static String driverName = "org.apache.hadoop.hive.jdbc.HiveDriver";
   
	public static void main(String[] args) {
		
		Class.forName(driverName);
		Connection conn=DriverManager.getConnection("jdbc:hive//localhost:10000/default","","");

		Statement stat=conn.createStatement();

		stat.executeQuery("CREATE DATABASE javadb");

		System.out.println("DATABASE created sucessfully..");

		conn.close();

	}
}




DROP DATABASE IF EXISTS temp;


CREATE TABLE IF NOT EXISTS employee(id int, name String ,salary String,designation String)COMMENT 'employee details'ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t' STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/home/manohar/resource/dataset/employee.txt'
OVERWRITE INTO TABLE employee;

DESCRIBE employee;

DROP TABLE employee;

Select count(*)from employee;

------------------------

CREATE TABLE txnrecords(txnno int, txndate String, custno int, amount Double, category String, product String, city String, state String, spendby String)
COMMENT 'transaction' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/home/manohar/resource/dataset/txns'
OVERWRITE INTO TABLE txnrecords

DESCRIBE txnrecords;

Select count(*) from txnrecords;

Select category, sum( amount) from txnrecords
group by category;



ALTER TABLE txnrecords RENAME TO txns;

ALTER TABLE txns CHANGE COLUMN spendby typeofpayment String;

ALTER TABLE txns ADD COLUMNS(dept String COMMENT 'department name');



DESCRIBE txns;


DROP TABLE IF EXISTS employee;


PARTITIONS;
------------------

ALTER TABLE txns ADD PARTITION (custno='4000007') LOCATION '/home/manohar/Desktop/';

------------------------------------------------------------------------

CREATE TABLE  name(firstname String)
COMMENT 'name details' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\n' STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/input/name.txt'
OVERWRITE INTO TABLE name;




CREATE EXTERNAL TABLE name(Name STRING)
	 Row format delimited
	 Fields terminated by '\n'
	 LOCATION '/input/';