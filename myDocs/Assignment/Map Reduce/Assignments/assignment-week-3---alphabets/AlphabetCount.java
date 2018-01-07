
import java.io.IOException;
import java.util.Iterator;
import java.util.StringTokenizer;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;
import org.apache.hadoop.mapred.TextInputFormat;
import org.apache.hadoop.mapred.TextOutputFormat;

public class AlphabetCount {
	
	
	public static class Mymapper extends MapReduceBase implements Mapper<LongWritable, Text, IntWritable, Text>{
		
		@Override
		
		public void map(LongWritable key, Text value, OutputCollector<IntWritable, Text> collector, Reporter reporter ) throws IOException{

			String line = value.toString();
			
			StringTokenizer tokenizer = new StringTokenizer(line);
			
			while (tokenizer.hasMoreTokens()){
				String word= tokenizer.nextToken();
				int size = word.length();
							
				collector.collect(new IntWritable(size), new Text(word));
			}
		}
	}
	
	public static class Myreducer extends MapReduceBase implements Reducer<IntWritable, Text, IntWritable, Text>{
		
		public void reduce( IntWritable key, Iterator<Text> values, OutputCollector<IntWritable, Text> collector , Reporter reporter) throws IOException{
			String finalword=null;
			int sum =0;
			while (values.hasNext()){
				sum++;	
				finalword=finalword+"->"+values.next().toString();
					
			}
			finalword = sum +" "+finalword  ;
			collector.collect(key, new Text(finalword));
		}
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub

		JobConf conf = new JobConf(AlphabetCount.class);
		
		conf.setJobName("albhabetcount");
		
		conf.setMapperClass(Mymapper.class);
		conf.setReducerClass(Myreducer.class);
		
		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);
	
		
		conf.setOutputKeyClass(IntWritable.class);
		conf.setOutputValueClass(Text.class);
		String inputpath="\\home\\cloudera\\Desktop\\alphabets.txt";
		String outputpath="\\home\\cloudera\\Desktop\\alpha";
		
		
		FileInputFormat.setInputPaths(conf, new Path(inputpath));
		FileOutputFormat.setOutputPath(conf, new Path(outputpath));
		
		JobClient.runJob(conf);

}

}