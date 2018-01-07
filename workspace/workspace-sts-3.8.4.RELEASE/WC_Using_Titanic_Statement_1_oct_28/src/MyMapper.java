import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable,Text,Text,IntWritable>{

	private final Text gender=new Text();
	private final IntWritable age=new IntWritable();
	
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		
		String line=value.toString();
		String []tokens=line.split(",");
		if (tokens.length>6) {
			if(tokens[1].equals("0"))
			{
				gender.set(tokens[4]);
				if(tokens[5].matches("\\d+"))
				{
					int i=Integer.parseInt(tokens[5]);
					age.set(i);
					context.write(gender, age);
				}
			}
		}
	}
}
