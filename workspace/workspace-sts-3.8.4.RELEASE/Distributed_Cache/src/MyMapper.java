import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.filecache.DistributedCache;

public class MyMapper extends Mapper<LongWritable,Text,Text,Text>{
	private Map<String,String> abmap=new HashMap<String,String>();
	private Text outputKey=new Text();
	private Text outputvalue=new Text();
	
	@Override
		protected void setup(Mapper<LongWritable, Text, Text, Text>.Context context)
				throws IOException, InterruptedException {
			Path[] files=DistributedCache.getLocalCacheFiles(context.getConfiguration());
				for (Path path : files) {
					if(path.getName().equals("abc.dat")){
						BufferedReader br=new BufferedReader(new FileReader(path.toString()));
						String line=br.readLine();
						while(line!=null){
							String []tokens=line.split("\t");
							String ab=tokens[0];
							String state=tokens[1];
							abmap.put(ab, state);
							line=br.readLine();
						}
					}
					
				}	
		}
@Override
protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
		throws IOException, InterruptedException {
		String line=value.toString();
		String token[]=line.split("\t");
		String state=abmap.get(token[0]);
		outputKey.set(state);
		outputvalue.set(line);
		context.write(outputKey, outputvalue);
}
}
