import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReducer extends Reducer<Text,IntWritable,Text, IntWritable>{

IntWritable intWrite=new IntWritable();
@Override
protected void reduce(Text key, Iterable<IntWritable> value,
		Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
	int sum=0;
	for (IntWritable foreachint : value) {
		sum=sum+foreachint.get();
	}
	intWrite.set(sum);
	context.write(key,intWrite);
}
}
