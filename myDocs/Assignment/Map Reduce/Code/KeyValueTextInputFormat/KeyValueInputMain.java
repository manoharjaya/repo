import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.KeyValueTextInputFormat;
import org.apache.hadoop.util.Tool;

public class KeyValueInputMain implements Tool
{
	public static void main(String[] args)
	{
		try
		{
			JobConf job = new JobConf(KeyValueInputMain.class);
			
    	    
    	    job.setJobName("Key Value Input Format");

    	    String[] itemsList = {"electronics","books","furniture","medicine","clothes","herbal","instruments"};
    		
    	    //job.setNumReduceTasks(0);
    	    //job.setNumReduceTasks(itemsList.length+1);// number of reducers
    	    
    	    
    	    job.set("mapreduce.input.keyvaluelinerecordreader.key.value.separator", "\t");   	    
    	    
    	    
    	    job.setMapperClass(KeyValueInputFormatMapper.class);
    	    job.setReducerClass(KeyValueInputFormatReducer.class);
    	    
    	    //job.setPartitionerClass(KeyValueInputPartitioner.class);    	    
    	    
    	    job.setMapOutputKeyClass(Text.class);
    	    job.setMapOutputValueClass(Text.class);
			
    	    job.setInputFormat(KeyValueTextInputFormat.class);
    	    
    	    
    	    FileInputFormat.setInputPaths(job, new Path(args[0]));
    		FileOutputFormat.setOutputPath(job, new Path(args[1]));
    		
    	    JobClient.runJob(job);
    	    
    	    
		}
		catch(Exception e)
		{
			e.printStackTrace();
			System.out.println("Error in main class: KeyValueInputMain");
		}
	}

	@Override
	public Configuration getConf() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void setConf(Configuration arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public int run(String[] arg0) throws Exception {
		// TODO Auto-generated method stub
		return 0;
	}
}
