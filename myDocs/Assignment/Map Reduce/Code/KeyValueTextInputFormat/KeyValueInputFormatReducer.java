

import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;

public class KeyValueInputFormatReducer extends MapReduceBase
implements Reducer<Text, Text, Text, Text>{	

	
	@Override
	public void reduce(Text input, Iterator<Text> value,
			OutputCollector<Text, Text> output, Reporter reporter) throws IOException 
	{
		
			String players = "";
			//String val= "";
			while(value.hasNext())
			{
				players += value.next() +",";
				//val = value.next().toString().trim();
				//System.out.println(players+"----- players----");
				
			}
			players = players.substring(0,players.lastIndexOf(','));
			output.collect(new Text(input+"="), new Text(players));
			
	}

}
