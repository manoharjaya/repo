import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable,Text,Text, IntWritable> {

	private Text text=new Text();
	private final IntWritable one=new IntWritable(1);
	
@Override
protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
		throws IOException, InterruptedException {
	StringTokenizer token=new StringTokenizer(value.toString());
	while(token.hasMoreElements())
	{
		String name=token.nextToken();
		text.set(name);
		context.write(text,one);
	}
}	
}
