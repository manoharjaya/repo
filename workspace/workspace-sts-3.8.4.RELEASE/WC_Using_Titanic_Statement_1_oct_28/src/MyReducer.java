import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReducer extends Reducer<Text,IntWritable,Text, IntWritable>{
	private final IntWritable age=new IntWritable();
	@Override
	protected void reduce(Text key, Iterable<IntWritable> value,
			Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
		
		int total=0,count=0;
		for (IntWritable eachAge : value) {
			count++;
			total+=eachAge.get();
		}
		total=total/count;
		age.set(total);
		context.write(key,age);
	}
}
