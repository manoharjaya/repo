import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.WritableComparable;

public class MyKey implements WritableComparable{

	private Text Survived,Sex;

	public MyKey() {
		Survived = new Text();
		Sex = new Text();
	}

	public MyKey(Text survived, Text sex) {
		Survived = survived;
		Sex = sex;
	}

	public Text getSurvived() {
		return Survived;
	}

	public void setSurvived(Text survived) {
		Survived = survived;
	}

	public Text getSex() {
		return Sex;
	}

	public void setSex(Text sex) {
		Sex = sex;
	}

	@Override
	public void readFields(DataInput in) throws IOException {
		Survived.readFields(in);
		Sex.readFields(in);
	}

	@Override
	public void write(DataOutput out) throws IOException {
		Survived.write(out);
		Survived.write(out);
	}

	@Override
	public int compareTo(Object o) {
		MyKey otherKey=(MyKey) o;
		int comp=Survived.compareTo(otherKey.Survived);
		if (comp!=0){
			return comp;
		}
		return comp=Sex.compareTo(otherKey.Sex);
	}	
}
