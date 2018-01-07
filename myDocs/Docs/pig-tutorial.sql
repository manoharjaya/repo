
		





		student= LOAD '/input/student' USING PigStorage('\t') AS (name:chararray,rollno:int);

		DUMP student;



		result = LOAD '/input/results' USING PigStorage('\t') as (rollno:int,status:chararray);
  
        Dump result;



        exec /home/manohar/myDocs/result.pig

        run /home/manohar/myDocs/result.pig    // statement should be on command history


        DESCRIBE result ;  

        ILLUSTRATE result;

        history;   

        groupdata= GROUP result BY status;

        DUMP groupdata;


        ILLUSTRATE groupdata;


        groupall= GROUP result ALL;

        DUMP groupall;



       	cogroupdata= COGROUP 


       	------------------------------------------------------------------------------------------

       	custs= LOAD '/input/custs' USING PigStorage(',') AS (id:int,f_name:chararray,l_name:chararray,age:int,occupation:chararray);

       	DUMP custs;

        txns= LOAD '/input/txns' USING PigStorage(',') AS (sno:chararray,dateofjoining:chararray,txns_id:int,amount:float,type_of_sports:chararray,games:chararray,city:chararray,state:chararray,payment_type:chararray);

        DUMP txns;

        groupcustsdata= GROUP custs BY  occupation;

        DUMP groupcustsdata;

        grouptxnsdata= GROUP txns BY type_of_sports;

        DUMP grouptxnsdata;

        cogroupcuststxnsdata= COGROUP custs BY id,txns BY txns_id;   //  it will return the results with two bags and common group 

        DUMP cogroupcuststxnsdata;

        







EXCERCISE
-------------------


student= LOAD '/input/student' USING PigStorage('\t') AS (name:chararray,rollno:int);

DUMP student;


ILLUSTRATE student;


result= LOAD '/input/results' USING PigStorage('\t') AS (rollno:int,status:chararray);

DUMP result;



STORE student INTO ' hdfs://localhost:9000/pig_Output/ ' USING PigStorage (',');



run /home/manohar/result.pig // run stored on history..

exec /home/manohar/result.pig





LOAD
-------


student_details = LOAD '/input/student_data.txt' USING PigStorage(',') AS (id:int, firstname:chararray, lastname:chararray, age:int, phone:chararray, city:chararray);


DUMP student_details;

GROUP
--------

groupdata= GROUP  student_details BY age;

DUMP groupdata;

GROUP MULTIPLE
---------------

group_multiple = GROUP student_details by (age, city);

DUMP group_multiple;

DESCRIBE
--------------

Describe groupdata;

GROUPALL
-----------

groupall = GROUP student_details ALL;

DUMP groupall;


employee_details = LOAD '/input/employee_details.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray)


DUMP employee_details;


COGROUP
--------

cogroupdata = COGROUP student_details BY age,employee_details BY age;

DUMP cogroupdata;


customerdata = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:float);

DUMP customerdata;

orderdata = LOAD '/input/orders.txt' USING PigStorage(',') AS (oid:int, date:chararray, customer_id:int, amount:int);

DUMP orderdata;

joindata = JOIN customerdata BY id, orderdata BY customer_id;

DUMP joindata;

JOIN
------

    1)
        SELF JOIN
        -----------

        customerdata1 = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:int);

        DUMP customerdata1;

        customerdata2= LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:int);

        DUMP customerdata2;

        joindata = JOIN customerdata1 BY id,customerdata2 BY id;


        DUMP joindata;

    2)
        INNER JOIN
        ------------


        customerdata = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:float);

        DUMP customerdata;

        orderdata = LOAD '/input/orders.txt' USING PigStorage(',') AS (oid:int, date:chararray, customer_id:int, amount:int);

        DUMP orderdata;

        joindata = JOIN customerdata BY id, orderdata BY customer_id;

        DUMP joindata;


    3)
        
        LEFT OUTER
        ------------

        customerdata = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:float);

        DUMP customerdata;

        orderdata = LOAD '/input/orders.txt' USING PigStorage(',') AS (oid:int, date:chararray, customer_id:int, amount:int);

        DUMP orderdata;

        joindata = JOIN customerdata BY id LEFT OUTER, orderdata BY customer_id;

        DUMP joindata;

    4)

        RIGHT OUTER
        ------------

        customerdata = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:float);

        DUMP customerdata;

        orderdata = LOAD '/input/orders.txt' USING PigStorage(',') AS (oid:int, date:chararray, customer_id:int, amount:int);

        DUMP orderdata;

        joindata = JOIN customerdata BY id RIGHT OUTER, orderdata BY customer_id;

        DUMP joindata;

    5)

        FULL OUTER
        ------------

        customerdata = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:float);

        DUMP customerdata;

        orderdata = LOAD '/input/orders.txt' USING PigStorage(',') AS (oid:int, date:chararray, customer_id:int, amount:int);

        DUMP orderdata;

        joindata = JOIN customerdata BY id FULL OUTER, orderdata BY customer_id;

        DUMP joindata;


CROSS
-------

        customerdata = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:float);

        DUMP customerdata;

        orderdata = LOAD '/input/orders.txt' USING PigStorage(',') AS (oid:int, date:chararray, customer_id:int, amount:int);

        DUMP orderdata;

        joindata = CROSS customerdata,orderdata;

        DUMP joindata;


UNION    //combine two result set..
------

The UNION operator of Pig Latin is used to merge the content of two relations. 
To perform UNION operation on two relations, their columns and domains must be identical.


        customerdata1 = LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:int);

        DUMP customerdata1;

        customerdata2= LOAD '/input/customers.txt' USING PigStorage(',') AS (id:int,name:chararray,age:int,city:chararray,salary:int);

        DUMP customerdata2;

        uniondata = UNION customerdata1,customerdata2;

        DUMP uniondata;


SPLIT         // split is like map reduce partition
-------

The SPLIT operator is used to split a relation into two or more relations.


    student_details = LOAD '/input/student_data.txt' USING PigStorage(',') AS (id:int, firstname:chararray, lastname:chararray, age:int, phone:chararray, city:chararray);

    SPLIT student_details into stu1 if age > 23 ,stu2 if (age >20 and age <=23) ;


    DUMP stu1;

    DUMP stu2;




FILTER
-----------

The FILTER operator is used to select the required tuples from a relation based on a condition.


    filterdata= FILTER student_details BY city=='Chennai';

    DUMP filterdata;

DISTINCT
----------
    

   student_details = LOAD '/input/student_data.txt' USING PigStorage(',') AS
   (id:int, firstname:chararray, lastname:chararray, phone:chararray, city:chararray);
    
    distinctdata = DISTINCT student_details;

    DUMP distinctdata;


FOREACH 
---------

    student_details = LOAD '/input/student_data.txt' USING PigStorage(',') AS
   (id:int, firstname:chararray, lastname:chararray, phone:chararray, city:chararray);
    
    DUMP student_details;
    
    foreachdata= FOREACH student_details GENERATE (id,firstname,city);

    DUMP foreachdata;


ORDER
-------

    
    student_details = LOAD '/input/student_data.txt' USING PigStorage(',') AS
   (id:int, firstname:chararray, lastname:chararray, phone:chararray, city:chararray);
    
    DUMP student_details;
    
    foreachdata= FOREACH student_details GENERATE (id,firstname,city);

    DUMP foreachdata;

    orderdata = ORDER foreachdata BY firstname DESC;

    DUMP orderdata;


LIMIT
-------


    student_details = LOAD '/input/student_data.txt' USING PigStorage(',') AS
   (id:int, firstname:chararray, lastname:chararray, phone:chararray, city:chararray);
    
    DUMP student_details;
    
    foreachdata= FOREACH student_details GENERATE (id,firstname,city);

    DUMP foreachdata;

    orderdata = ORDER foreachdata BY firstname DESC;

    DUMP orderdata;


    limitdata = LIMIT orderdata  5;
    
    DUMP limitdata;




---------------------------------------------------



UDF
-------










-----------------------------------------


ps1
----
    
        List the movies that having a rating greater than 4



        moviesdata  = LOAD '/input/movies_ratings.txt' USING PigStorage(',') AS (sno:int,moviename:chararray,yearofrelease:int,rating:chararray,fare:int);

        DUMP moviesdata;


        filterdata = FILTER moviesdata BY rating if rating > 4 ;













--------------------------------




        A = load '/input/DelayedFlights.csv' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',','NO_MULTILINE','UNIX','SKIP_INPUT_HEADER');

