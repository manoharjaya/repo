import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import org.apache.hadoop.mapreduce.lib.input.LineRecordReader;

public class MyRecordReader extends RecordReader<MyKey, IntWritable> {

	private MyKey key;
	private IntWritable value;
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
	public IntWritable getCurrentValue() throws IOException, InterruptedException {
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
		boolean getkeyvalue=reader.nextKeyValue();
		if (getkeyvalue) {
			if(key==null)
			{
				key=new MyKey();
			}
			if(value==null)
			{
				value=new IntWritable();
			}
			Text line=reader.getCurrentValue();
			String[] tokens=line.toString().split(",");
			key.setSurvived(new Text(tokens[1]));
			key.setSex(new Text(tokens[4]));
			value.set(new Integer(1));
		}
		return getkeyvalue;
	}

}
