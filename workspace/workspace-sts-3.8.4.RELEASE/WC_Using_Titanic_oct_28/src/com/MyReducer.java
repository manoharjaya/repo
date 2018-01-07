package com;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReducer extends Reducer<Text,IntWritable,Text,IntWritable>{
	
	
	@Override
	protected void reduce(Text key, Iterable<IntWritable> value,
			Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
		
		String tempKey=key.toString();
		int sum=0;
		for (IntWritable intWritable : value) {
			sum=sum+intWritable.get();
		}
		context.write(key,new IntWritable(sum));
		
	}
}
