

import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.Partitioner;

public class KeyValueInputPartitioner implements Partitioner<Text, Text> 
{
	
	

	@Override
	public void configure(JobConf job) 
	{
		
	// initlialize new jonConf passed	
	}

	/**
	 * key is mapper key and value is mapper output
	 */
	@Override
	public int getPartition(Text key, Text value, int numofReducers) 
	{
		/**
		 * number of partitioners = number of reducers
		 */
		
		String[] itemsList = {"electronics","books","furniture","medicine","clothes","herbal","instruments"};
		
		
		/*
		for(int i=0;i<numofReducers;i++)
		{
			//return i;
		}
		*/
		if(key.toString().equals(itemsList[0]))
		{
			return 0;
		}
		if(key.toString().equals(itemsList[1]))
		{
			return 1;
		}
		if(value.toString().equals(itemsList[2]))
		{
			return 2;
		}
		if(value.toString().equals(itemsList[3]))
		{
			return 3;
		}
		if(value.toString().equals(itemsList[4]))
		{
			return 4;
		}
		if(value.toString().equals(itemsList[5]))
		{
			return 5;
		}
		if(value.toString().equals(itemsList[6]))
		{
			return 6;
		}
		else
		{
			return 7;
		}
		
	}

}
