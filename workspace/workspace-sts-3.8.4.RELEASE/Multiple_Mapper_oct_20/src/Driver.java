import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class Driver extends Configured implements Tool{
	
	
	public static void main(String[] args) throws Exception {
		int result=ToolRunner.run(new Configuration(),new Driver(), args);
		System.exit(result);
	}

	@Override
	public int run(String[] arg0) throws Exception {
		
		Configuration conf=this.getConf();
		Job job=Job.getInstance(conf, "Multiple_Mapper_oct_20");
		job.setJarByClass(Driver.class);
		
		MultipleInputs.addInputPath(job, new Path(arg0[0]),TextInputFormat.class,MyMapper1.class);
		MultipleInputs.addInputPath(job, new Path(arg0[1]),TextInputFormat.class,MyMapper2.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);
		
		job.setReducerClass(MyReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		Path outdir=new Path(arg0[2]);
		FileSystem fs =FileSystem.get(conf);
		fs.delete(outdir);
		
		FileOutputFormat.setOutputPath(job, outdir);
		
		return job.waitForCompletion(true)?0:1;
	}
}
