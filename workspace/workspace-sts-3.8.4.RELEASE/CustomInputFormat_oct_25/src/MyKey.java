import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.WritableComparable;

public class MyKey implements WritableComparable{

	private Text SensorType,timestamp,status;
	
	public MyKey() {
		this.SensorType = new Text();
		this.timestamp = new Text();
		this.status = new Text();
	}

	public MyKey(Text sensorType, Text timestamp, Text status) {
		SensorType = sensorType;
		this.timestamp = timestamp;
		this.status = status;
	}

	@Override
	public void readFields(DataInput in) throws IOException {
		SensorType.readFields(in);
		timestamp.readFields(in);
		status.readFields(in);
	}

	@Override
	public void write(DataOutput out) throws IOException {
		SensorType.write(out);
		timestamp.write(out);
		status.write(out);
	}

	@Override
	public int compareTo(Object o) {
		MyKey otherkey=(MyKey)o;
		int test=SensorType.compareTo(otherkey.SensorType);
		if(test!=0)
			return test;
		test=timestamp.compareTo(otherkey.timestamp);
		if (test!=0)
			return test;
		test=status.compareTo(otherkey.status);
		return test;
	}

	public Text getSensorType() {
		return SensorType;
	}

	public void setSensorType(Text sensorType) {
		SensorType = sensorType;
	}

	public Text getTimestamp() {
		return timestamp;
	}

	public void setTimestamp(Text timestamp) {
		this.timestamp = timestamp;
	}

	public Text getStatus() {
		return status;
	}

	public void setStatus(Text status) {
		this.status = status;
	}
}
