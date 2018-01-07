package com;

import java.io.IOException;

import org.apache.hadoop.io.Text;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class Driver {
public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
	
	Configuration conf=new Configuration();
	Job job=Job.getInstance(conf, "WC_oct_17");
	
	job.setJarByClass(Driver.class);
	job.setMapperClass(MyMapper.class);
	job.setCombinerClass(MyReducer.class);
	job.setReducerClass(MyReducer.class);
	
	job.setMapOutputKeyClass(Text.class);
	job.setMapOutputValueClass(IntWritable.class);
	
	job.setOutputKeyClass(org.apache.hadoop.io.Text.class);
	job.setOutputValueClass(IntWritable.class);
	
	
	job.setInputFormatClass(TextInputFormat.class);
	job.setOutputFormatClass(TextOutputFormat.class);
	
	FileInputFormat.setInputPaths(job,args[0]);
	
	Path output=new Path(args[1]);
	FileSystem fs=FileSystem.get(conf);
	fs.delete(output);
	
	FileOutputFormat.setOutputPath(job,output);
	
	System.exit(job.waitForCompletion(true)?0:1);
	
	
}
}
