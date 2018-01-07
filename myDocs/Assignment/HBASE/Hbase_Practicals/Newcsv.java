package hbtest;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.ResultScanner;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.util.Bytes;
public class Newcsv {
public static void main(String[] args) throws IOException {

String csvfile = "/home/cloudera/Desktop/test/nyse";
String line;
int row= 0;

Configuration config = HBaseConfiguration.create();
HTable table = new HTable(config, "mycsv");
Put p ;

BufferedReader br = new BufferedReader(new FileReader(csvfile));

while((line = br.readLine())!=null){
	row++;
	String value[] = line.split(",");
    String rowid = Integer.toString(row);
	p = new Put(Bytes.toBytes(rowid));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col1"),Bytes.toBytes(value[0]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col2"),Bytes.toBytes(value[1]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col3"),Bytes.toBytes(value[2]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col4"),Bytes.toBytes(value[3]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col5"),Bytes.toBytes(value[4]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col6"),Bytes.toBytes(value[5]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col7"),Bytes.toBytes(value[6]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col8"),Bytes.toBytes(value[7]));
	p.add(Bytes.toBytes("myFamily"), Bytes.toBytes("Col9"),Bytes.toBytes(value[8]));
	table.put(p);
	
	//System.out.println("Value : "+ value[8]);
}
}
}

