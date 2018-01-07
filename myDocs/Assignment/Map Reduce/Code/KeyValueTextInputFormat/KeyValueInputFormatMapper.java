

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;

public class KeyValueInputFormatMapper 
extends MapReduceBase implements Mapper<Text, Text, Text, Text>
{

	@Override
	public void map(Text key, Text value, OutputCollector<Text, Text> output,
			Reporter reporter) throws IOException 
	{
		//	key www.croma.com
		//	value tvs, electronics, Appliances
		
		//	Expected Output as :
		//	tvs,www.croma.com
		//	electronics,www.croma.com
		//	Appliances,www.croma.com
		
		
		//StringTokenizer st = new StringTokenizer(input.toString(), "\t");
		String[] aray = value.toString().split("\t");
		
		
		
			String[] valueAray = value.toString().split(",");
			
			for(int j=0;j<valueAray.length;j++)
			{
				//output.collect(new Text(aray[i]), new Text(valueAray[j]));
				output.collect(new Text(valueAray[j]), key);
			}
			
		}
	}

	

