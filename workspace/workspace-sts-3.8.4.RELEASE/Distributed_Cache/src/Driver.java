import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.filecache.DistributedCache;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class Driver extends Configured implements Tool{

	public static void main(String[] args) throws  Exception {

		int result=ToolRunner.run(new Configuration(),new Driver(), args);
		System.exit(result);
		
	}

	@Override
	public int run(String[] arg0) throws Exception {

		Configuration conf=this.getConf();
		
		Job job=Job.getInstance(conf, "Distributed_Cache_oct_19");
		job.setJarByClass(Driver.class);
		
		job.setMapperClass(MyMapper.class);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);
		
		job.setNumReduceTasks(0);

		try
		{
			DistributedCache.addCacheFile(new URI("/input/abc.dat"),job.getConfiguration());    //Do not change
		}
		catch (Exception e) {
			System.out.println(e);
		}
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		FileInputFormat.setInputPaths(job, arg0[0]);
		
		Path output=new Path(arg0[1]);
		FileSystem fs=FileSystem.get(conf);
		fs.delete(output);
		
		FileOutputFormat.setOutputPath(job,output);

		return job.waitForCompletion(true)?0:1;
	}

}
