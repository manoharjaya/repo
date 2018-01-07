import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

public class MyPartitioner extends Partitioner<Text,IntWritable>{

	@Override
	public int getPartition(Text key, IntWritable value, int arg2) {
		String token=key.toString();
		if(token.equals("manohar"))
			return 0;
		else if(token.equals("lakshman"))
			return 1;
		else
			return 2;
	}

}
