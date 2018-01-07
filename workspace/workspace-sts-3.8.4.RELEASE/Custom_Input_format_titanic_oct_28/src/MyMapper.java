import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<MyKey,IntWritable,Text,IntWritable>{

	private final static IntWritable one = new IntWritable(1);
	@Override
	protected void map(MyKey key, IntWritable value, Mapper<MyKey, IntWritable, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
	
		String newKey=key.getSurvived()+","+key.getSex();
		context.write(new Text(newKey), one);
	
	}
}
