







         									Hadoop Base Commands
         									

    hadoop dfsadmin -safemode get

	hadoop dfsadmin -safemode leave    

	hadoop fs -ls /input

	hadoop fs -cat /input/test*

	hadoop fs -put /home/manohar/resource/dataset/test.txt  /input

	hadoop jar /home/manohar/test.jar fam.manohar.count.DriverClass  /input/test.txt /output/


	                                        BY USING TOOL INTERFACE  (-D mapred.reduce.tasks=2)

hadoop jar /home/manohar/resource/mrjar/WC_partitioner_oct_17.jar Driver -D mapred.reduce.tasks=2 /input/name.txt /output/wc_partitioner_oct_17



logs -> /home/manohar/hadoop/logs/userlogs


------------------------------------------------------------------------------------------------------------

                                                  MAP REDUCE
                                               ----------------




											DISTRIBUTED CACHE
											------------------

DriverClass
------------------
     try
		{
			DistributedCache.addCacheFile(new URI("/input/abc.dat"),job.getConfiguration());    //Do not change
		}
		catch (Exception e) {
			System.out.println(e);
		}
-------------------------------------------------------------

MapperClass
-----------------

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



----------------------------------------------------------------------------------------------------------

												COMBINERCLASS
												--------------

DriverClass
-------------

Configuration conf=this.getConf();
	
	Job job=Job.getInstance(conf, "combiner class");
	job.setJarByClass(Driver.class);
	
	job.setMapperClass(MyMapper.class);
	job.setCombinerClass(MyReducer.class);   //set combiner class
	
	
	job.setReducerClass(MyReducer.class);
	

---------------------------------------------------------------------------------------------------------

										PARTITIONERCLASS
										------------------

MyPartitioner
-------------

@Override
	public int getPartition(Text key, IntWritable value, int arg2) {
		String token=key.toString();
		if(token.equals("manohar"))
			return 0;
		else if(token.equals("lakshman"))
			return 1;
		else
			return 2;
	}

---------------------------------------------------

DriverClass
------------

    Configuration conf=this.getConf();
	
	Job job=Job.getInstance(conf, "Partitioner class");
	job.setJarByClass(Driver.class);
	
	
	job.setNumReduceTasks(3);    // set reducer output to 3
	
	job.setMapperClass(MyMapper.class);
	job.setCombinerClass(MyReducer.class);   //set combiner class
	
	job.setReducerClass(MyReducer.class); 
	job.setPartitionerClass(MyPartitioner.class);  // output generate based on data 
	
	// manohar   r0
	//lakshman	 r1
	
	/*
	 * ravi      r2
	 * ram
	 * shekhar
	 * */
	
	
	job.setOutputKeyClass(Text.class);
	job.setOutputValueClass(IntWritable.class);
	
	job.setInputFormatClass(TextInputFormat.class);
	job.setOutputFormatClass(TextOutputFormat.class);
	
	FileInputFormat.setInputPaths(job, arg0[0]);
	Path output=new Path(arg0[1]);
	FileSystem fs=FileSystem.get(conf);
	fs.delete(output);
	
	
	FileOutputFormat.setOutputPath(job,output);
	return  job.waitForCompletion(true)?0:1;

-----------------------------------------------------------------------------------------------------------
							
							         	MULTIPLE MAPPER
						         	------------------------


DRIVERCLASS
--------------

        Configuration conf=this.getConf();
		Job job=Job.getInstance(conf, "Multiple_Mapper_oct_20");
		job.setJarByClass(Driver.class);
		
		MultipleInputs.addInputPath(job, new Path(arg0[0]),TextInputFormat.class,MyMapper1.class);
		MultipleInputs.addInputPath(job, new Path(arg0[1]),TextInputFormat.class,MyMapper2.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);

---------------------------------------------------

MAPPERCLASS1
-------------

         String line=value.toString();
		 String []token=line.split(",");
		 outputKey.set(token[0]);
		 outputValue.set("cust\t"+token[1]);
		 context.write(outputKey, outputValue);  // 4000001,cust\tkrishna


---------------------------------------------------

MAPPERCLASS2
--------------

         String line=value.toString();
		 String []token=line.split(",");
		 outputKey.set(token[2]);
		 outputValue.set("txn\t"+token[3]);
		 context.write(outputKey, outputValue);   // <4000001,txn\t40.00>

---------------------------------------------------

REDUCERCLASS
--------------
		
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

-------------------------------------------------------------------------------------------------------------


