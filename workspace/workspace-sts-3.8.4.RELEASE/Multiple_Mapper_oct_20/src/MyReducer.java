import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReducer extends Reducer<Text,Text, Text,Text>{

	private Text outputKey=new Text();
	private Text outputValue=new Text();
	
	@Override
	protected void reduce(Text key, Iterable<Text> value, Reducer<Text, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		
		String name = null;
		int count = 0;
		double price = 0;
		for (Text text : value) 
		{
			String token[]=text.toString().split("\t");
			if(token[0].equals("cust"))
				name=token[1];
			else if(token[0].equals("txn"))
			{
				count++;
				price+=Float.parseFloat((token[1])); 
			}
		}
		String changeFormat=String.format("%d\t%f",count,price);
		System.out.println("manohar="+changeFormat+"\t"+name);
		outputKey.set(name);
		outputValue.set(changeFormat);
		context.write(outputKey, outputValue);
	}
}
 