import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable,Text,Text,Text>{
	private final Text pclass=new Text();
	private final Text compositeValue=new Text();
	
@Override
protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
		throws IOException, InterruptedException {
	// TODO Auto-generated method stub
	
	String line=value.toString();
	String []tokens=line.split(",");
	if(tokens.length>6)
	{
		String mulvalue=tokens[1]+" "+tokens[4]+" "+tokens[5];
		String cls=tokens[2];
		pclass.set(cls);
		compositeValue.set(mulvalue);
		context.write(compositeValue,pclass);
	}
}
}
