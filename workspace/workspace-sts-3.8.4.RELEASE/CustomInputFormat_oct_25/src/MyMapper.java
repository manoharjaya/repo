import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<MyKey, MyValue, Text, Text>{

	
	@Override
	protected void map(MyKey key, MyValue value, Mapper<MyKey, MyValue, Text, Text>.Context context)
			throws IOException, InterruptedException {
		
		 String sensor = key.getSensorType().toString()+""+key.getTimestamp();
         
//         if(sensor.toLowerCase().equals("a")){
//         	context.write(value.getValue1(),value.getValue2());
//         }
		 context.write(new Text(sensor), value.getValue1());
	}
}
