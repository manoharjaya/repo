result = LOAD '/input/results' USING PigStorage('\t') as (rollno:int,status:chararray);
  
Dump result;