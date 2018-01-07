import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper2 extends Mapper<LongWritable,Text,Text,Text>{
	
	private Text outputKey=new Text();
	private Text outputValue=new Text();
	
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		 String line=value.toString();
		 String []token=line.split(",");
		 outputKey.set(token[2]);
		 outputValue.set("txn\t"+token[3]);
		 context.write(outputKey, outputValue);   // <400001,txn\t40.00>
	}

}
