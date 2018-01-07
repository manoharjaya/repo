import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import org.apache.hadoop.mapreduce.lib.input.LineRecordReader;

public class MyRecordReader extends RecordReader<MyKey, MyValue> {

	private MyKey key;
	private MyValue value;
	private LineRecordReader reader = new LineRecordReader();
	@Override
	public void close() throws IOException {
		reader.close();
	}

	@Override
	public MyKey getCurrentKey() throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		return key;
	}

	@Override
	public MyValue getCurrentValue() throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		return value;
	}

	@Override
	public float getProgress() throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		return reader.getProgress();
	}

	@Override
	public void initialize(InputSplit arg0, TaskAttemptContext arg1) throws IOException, InterruptedException {
		reader.initialize(arg0, arg1);

	}

	@Override
	public boolean nextKeyValue() throws IOException, InterruptedException {
		boolean gotNextKeyValue = reader.nextKeyValue();
		System.out.println("manohar gotNextKeyValue="+gotNextKeyValue);
		if (gotNextKeyValue) {
			if (key==null) {
				key=new MyKey();
			}
			if (value==null) {
				value=new MyValue();
			}
			Text line=reader.getCurrentValue();
			System.out.println("manohar line="+line);
			String[] tokens=line.toString().split("\t");
			for (String string : tokens) {
				System.out.println("manohar tokens="+string);
			}
			
			key.setSensorType(new Text(tokens[0]));
			key.setTimestamp(new Text(tokens[1]));
			key.setStatus(new Text(tokens[2]));
			value.setValue1(new Text(tokens[3]));
			value.setValue2(new Text(tokens[4]));
		}
		else {
			key = null;
			value = null;
		}
		return gotNextKeyValue;
	}

}
