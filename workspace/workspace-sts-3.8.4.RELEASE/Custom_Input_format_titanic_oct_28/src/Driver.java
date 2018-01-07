import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class Driver extends Configured implements Tool{

	public static void main(String[] args) throws Exception {
		int getResult=ToolRunner.run(new Configuration(),new Driver(), args);
		System.exit(getResult);
	}

	@Override
	public int run(String[] arg0) throws Exception {
		
		Configuration conf=this.getConf();
		Job job=Job.getInstance(conf, "Custom_input_format_titanic_oct_28");
		job.setJarByClass(Driver.class);
		
		
		job.setInputFormatClass(MyInputFormat.class);
		
		job.setMapperClass(MyMapper.class);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(IntWritable.class);
		
		job.setReducerClass(MyReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		job.setOutputFormatClass(TextOutputFormat.class);
		
		FileInputFormat.setInputPaths(job, arg0[0]);
		
		Path ourDir=new Path(arg0[1]);
		FileSystem fs=FileSystem.get(conf);
		fs.delete(ourDir);
		
		
		FileOutputFormat.setOutputPath(job, ourDir);
		
		return job.waitForCompletion(true)?0:1;
	}
}
