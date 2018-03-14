	

						systemctl stop mysqld.service 

						

                         ADMIN ACCESS FOR CREATE AND DROP A TABLE

	                         mysqladmin -u root -p create test

	                         mysqladmin -u root -p drop test


	                        create database if not exists temp;

	                        	
  -----------------------------------------------------------------------------


  									CREATE TABLE


  							CREATE TABLE customer(
								cust_id INT NOT NULL AUTO_INCREMENT,
  								first_name VARCHAR(50) NOT NULL ,
  								last_naem VARCHAR(50) NOT NULL,
  								address1 VARCHAR(50) NOT NULL,
  								address2 VARCHAR(50)  NULL,
  								country VARCHAR(50) NOT NULL,
  								PRIMARY KEY(cust_id));






  									 show databases;

  									 use test;

  									 show tables;

  									 show column from customer;   

  									 	or

  									 desc customer;


  									 show index from customer;   //show PRIMARY KEY

  									 show create tables customer; //show cretaed tables syntax

-----------------------------------------------------------------------------------------------------------------

  									 DROP TABLE


  									 DROP TABLE customer;

-----------------------------------------------------------------------------------------------------------------

  									INSERT QUERY


  									INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES("manohar","jaya","vile parle","mumbai","india");
  									INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES("ram","kaunder","vile parle","mumbai","india");
  									INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES("lakshman","kaunder","vile parle","mumbai","india");
  									INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES("ravi","kaunder","vile parle","mumbai","india");
  									INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES("shekhar","kaunder","vile parle","mumbai","india");
  									
  									INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES("jaya","kaunder","vile parle","mumbai","india");
  									INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES("dhanush","kaunder","vile parle","mumbai","india");
  									

  									INSERT INTO customer VALUES("shekhar","kaunder","vile parle","mumbai","india");
  									
  									INSERT INTO customer VALUES("shekhar","kaunder","vile parle","mumbai","india"),
  																("shekhar","kaunder","vile parle","mumbai","india"),
  																("shekhar","kaunder","vile parle","mumbai","india");
--------------------------------------------------------------------------------------------------------------

								
									SELECT QUERY


							SELECT * FROM customer WHERE first_name="ram";

							SELECT * FROM customer WHERE cust_id<=2;

							SELECT * FROM customer WHERE cust_id!=2;

							SELECT * FROM customer WHERE cust_id=2;

------------------------------------------------------------------------------------------------------
	
								UPDATE QUERY

							UPDATE  customer SET first_name="Manohar" WHERE cust_id=1 

---------------------------------------------------------------------------------------------------------

								DELETE QUERY


						DELETE FROM customer WHERE cust_id=1 AND first_name="manohar";

						DELETE FROM customer;  // DELETE all contents from table


---------------------------------------------------------------------------------------------------

				

						 ALTER TABLE (ADD, DROP, MODIFY, CHANGE COLUMN, RENAME TO)




			ALTER TABLE customer ADD state VARCHAR(50) NOT NULL AFTER address2;

			ALTER TABLE customer MODIFY address2 VARCHAR(100) NOT NULL ;

			ALTER TABLE customer DROP state ;

			ALTER TABLE customer CHANGE COLUMN last_naem last_name VARCHAR(20) NOT NULL AFTER first_name;  // RENAME COLUMN

			ALTER TABLE customer RENAME TO cust;

--------------------------------------------------------------------------------------------------------

									TRUNCATE TABLE

				TRUNCATE TABLE customer;

--------------------------------------------------------------------------------------------------------

									


		CREATE TABLE sales(

			sales_id int NOT NULL AUTO_INCREMENT , price float(2,2) NOT NULL, territory VARCHAR(5) NOT NULL);


		INSERT INTO sales VALUES(25,"south"),(10,"north"),(22,"west"),(12,"west");
		


		ALTER TABLE sales MODIFY price tinyint NOT NULL ;

		ALTER TABLE sales CHANGE COLUMN price cost tinyint NOT NULL AFTER sales_id;

		ALTER TABLE sales RENAME TO salesman;

----------------------------------------------------------------------------------------------------------------



			CREATE TABLE product(p_id INT NOT NULL AUTO_INCREMENT,p_name VARCHAR(50) NOT NULL ,qty VARCHAR(50) NOT NULL,PRIMARY KEY(p_id));



			INSERT INTO product (p_name,qty) VALUES("TV","100");
			INSERT INTO product (p_name,qty) VALUES("fridge","152");
			INSERT INTO product (p_name,qty) VALUES("AC","200");
  			INSERT INTO product (p_name,qty) VALUES("Washing machine","100");	


  			TRUNCATE TABLE product;



  			----------------------------------------------------------------------------------------------




  			CREATE database retail;

  			use retail;

  			CREATE TABLE product(p_id INT,p_name STRING,qty STRING);


---------------------------------------------------------------------------------------------------

											JOINS

				SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory from customer AS c INNER JOIN  salesman AS s
				ON c.cust_id=s.sales_id;

				SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory from customer AS c LEFT OUTER JOIN salesman AS s
				ON c.cust_id=s.sales_id;

			
				SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory from customer AS c RIGHT OUTER JOIN salesman AS s
				ON c.cust_id=s.sales_id;


-----------------------------------------------------------------------------------------------------------


									       WHERE CLAUSE


				SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory from customer AS c LEFT OUTER JOIN salesman AS s
				ON c.cust_id=s.sales_id WHERE c.first_name="manohar";

------------------------------------------------------------------------------------------------------------

										     DISTINCT


				SELECT DISTINCT s.cost, c.cust_id, c.first_name, c.address1, c.country, s.territory from customer AS c LEFT OUTER JOIN salesman AS s ON c.cust_id=s.sales_id;

-----------------------------------------------------------------------------------------------------------------------------------

											ORDER BY (ASC,DESC)


				SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory from customer AS c RIGHT OUTER JOIN salesman AS s ON c.cust_id=s.sales_id ORDER BY c.cust_id DESC;

				SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory from customer AS c RIGHT OUTER JOIN salesman AS s ON c.cust_id=s.sales_id ORDER BY c.first_name ASC;


---------------------------------------------------------------------------------------------------------------------


			
										      GROUP BY

				SELECT SUM(cost) AS territory_cost, territory , first_name  FROM salesman INNER JOIN customer ON sales_id =cust_id GROUP BY territory ORDER BY first_name ASC

				SELECT SUM(cost) AS territory_cost, territory , first_name  FROM salesman INNER JOIN customer ON sales_id =cust_id   GROUP  BY ORDER BY territory ASC HAVING SUM(cost) AS territory_cost => 35;


											HAVING CLAUSE

			SELECT SUM(cost) AS territory_cost, territory , first_name  FROM salesman INNER JOIN customer ON sales_id =cust_id GROUP BY territory HAVING SUM(cost)>35  ORDER BY territory_cost ASC;


-------------------------------------------------------------------------------------------------------------------------------------

				

											    LIKE (%,_)


			SELECT * FROM customer WHERE first_name LIKE "manohar";

			SELECT * FROM customer WHERE first_name LIKE "mano%";

			SELECT * FROM customer WHERE first_name LIKE "mano_ar";

			SELECT * FROM customer WHERE first_name LIKE "_anohar";


			SELECT * FROM customer WHERE first_name NOT LIKE "mano%";


------------------------------------------------------------------------------------------------------------------------------------


												IN (eg. OR | replace OR)

				SELECT * FROM customer WHERE first_name IN ("manohar","shekhar","ram","lakshman");


											CONTRAST WITH

				SELECT * FROM customer WHERE first_name ="manohar" OR first_name="shekhar" OR first_name="ram" OR first_name="lakshman";



-----------------------------------------------------------------------------------------------------------------------------------
												
												NOT(opposite of MySQL IN condition)	

			
			    SELECT * FROM customer WHERE first_name NOT IN ("manohar");

			    SELECT * FROM customer WHERE first_name NOT IN ("manohar","shekhar","ram","lakshman");


			    SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory FROM customer AS c RIGHT OUTER JOIN salesman AS s ON c.cust_id=s.sales_id WHERE c.first_name IS  NOT NULL;
			    

			    SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory FROM customer AS c RIGHT OUTER JOIN salesman AS s ON c.cust_id=s.sales_id WHERE c.first_name IS NULL;

			    SELECT c.cust_id, c.first_name, c.address1, c.country, s.cost, s.territory FROM customer AS c RIGHT OUTER JOIN salesman AS s ON c.cust_id=s.sales_id WHERE c.cust_id NOT BETWEEN 1 AND 3;


--------------------------------------------------------------------------------------------------------------------------------------


									         eg	. FIRST AND LAST RECORD


				SELECT * FROM customer LIMIT 1;

				SELECT * FROM customer ORDER BY cust_id DESC LIMIT 2;

				SELECT * FROM salesman LIMIT 3,2;      //  (3,2)   AFTER 3 row display only 2 rows



---------------------------------------------------------------------------------------------------------------------------------------



												DATE 

			SELECT CURRENT_DATE(); 

			SELECT NOW();






















EXCERCISE
--------------------------






CREATE TABLE student(
	s_id int NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(50) NOT NULL UNIQUE,
	last_name VARCHAR(50) NOT NULL,
	address1 VARCHAR(50) NOT NULL,
	address2 VARCHAR(50) NOT NULL,
	country VARCHAR(50) NOT NULL,
	phone VARCHAR(12) NOT NULL UNIQUE,
	PRIMARY KEY(s_id));





INSERT INTO student(first_name,last_name,address1,address2,country,phone)VALUES
('manohar','jaya','vile parle','mumbai','india','9877878445'),('jaya','p','vile parle','mumbai','india','4454587788');


INSERT INTO student(first_name,last_name,address1,address2,country,phone)VALUES
('lakshman','gounder','vile parle','mumbai','india','9457877745'),('ram','gounder','vile parle','mumbai','india','4545478124'),
('ravi','gounder','vile parle','mumbai','india','4448745481'),('shekhar','gounder','vile parle','mumbai','india','4724466632');


SELECT * FROM student ORDER BY s_id desc \G;

SHOW CREATE TABLE student \G;


SHOW INDEX FROM student \G;



DROP TABLE student;


SELECT * FROM student WHERE s_id>2 ;

SELECT * FROM student WHERE s_id!=4 ;

SELECT * FROM student WHERE s_id!=4 AND s_id<=2;


SELECT * FROM student WHERE s_id!=4 OR s_id<=1;


SELECT * FROM student WHERE first_name='jaya';

SELECT *  FROM student;



UPDATE student SET first_name='Manohar' WHERE first_name="manohar";



DELETE FROM student WHERE first_name='Manohar' AND s_id=1 AND last_name='jaya';


DELETE FROM student;


INSERT INTO student (first_name,last_name,address1,address2,country,phone)VALUES
('Manohar','jaya','vile parle','mumbai','india','889898987');




ALTER TABLE student ADD designation VARCHAR(50) NOT NULL AFTER last_name;

ALTER TABLE student MODIFY phone VARCHAR(15)  NULL;

ALTER TABLE student CHANGE COLUMN last_name l_name VARCHAR(15) NOT NULL;

ALTER TABLE student DROP designation;

ALTER TABLE stu RENAME TO student;




TRUNCATE TABLE student; // TRUNCATE is DDL  command is cannot be roll back but in delete is a DML command is copied on 
						on rollback tablespace when you are even delete the RECORD you can get it later while using DELETE

						//TRUNCATE is faster than DELETE because it is not stored on rollback tablespaces



CREATE TABLE progress(
	p_id int NOT NULL AUTO_INCREMENT,
	subject1 VARCHAR(15) NOT NULL,
	subject2 VARCHAR(15) NOT NULL,
	marks tinyint NOT NULL,
	PRIMARY KEY(p_id));


SELECT * FROM progress;


INSERT INTO progress(subject1,subject2,marks)VALUES('science','maths',70),('chmistry','physics',50),
('computer','electronics',70);


SELECT * FROM student INNER JOIN progress on s_id=p_id;



ALTER TABLE student CHANGE COLUMN l_name last_name VARCHAR(20) NOT NULL;



SELECT * FROM student AS stu INNER JOIN progress as pro ON stu.s_id=pro.p_id ORDER BY stu.s_id DESC;


SELECT * FROM student AS stu LEFT OUTER JOIN progress as pro ON stu.s_id=pro.p_id ORDER BY stu.s_id DESC;


SELECT * FROM student AS stu RIGHT OUTER JOIN progress as pro ON stu.s_id=pro.p_id ORDER BY stu.s_id DESC;


SELECT * FROM student AS stu LEFT OUTER JOIN progress as pro ON stu.s_id=pro.p_id WHERE first_name="manohar" ORDER BY stu.s_id DESC ;


SELECT DISTINCT stu.last_name,stu.first_name,stu.country,pro.subject1,pro.subject2,pro.marks FROM student AS stu LEFT OUTER JOIN progress as pro ON stu.s_id=pro.p_id WHERE first_name="manohar" ORDER BY stu.s_id DESC ;



select count(last_name), first_name  from student group by last_name ;


SELECT * FROM student WHERE first_name LIKE "manohar";


SELECT * FROM student WHERE first_name LIKE "mano%";


SELECT * FROM student WHERE first_name LIKE "mano_ar";


SELECT * FROM student WHERE first_name LIKE "_ano";   // empty


SELECT * FROM student WHERE first_name NOT LIKE "mano_ar";


SELECT * FROM student WHERE first_name IN('manohar','jaya','lakshman');

SELECT * FROM student WHERE first_name NOT IN("manohar");



SELECT * FROM  student LIMIT 3,2;  


SELECT CURRENT_DATE();





CREATE TABLE employee
(
	e_id tinyint NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	work_date VARCHAR(50) NOT NULL,
	daily_typed_pages VARCHAR(50) NOT NULL,
	PRIMARY KEY(e_id)
);


INSERT INTO employee(name,work_date,daily_typed_pages)VALUES
('manohar','03-15-1995','700'),('jaya','03-15-1995','500'),('manohar','03-15-1995','720'),
('jaya','03-15-1995','900'),('lakshman','04-15-1995','500'),('ram','04-15-1995','2500'),('ram','04-15-1995','700');



SELECT COUNT(*),name from employee GROUP BY name;








mysqladmin -uroot -p SELECT * FROM employee INTO OUTFILE '/home/manohar/employee.txt';













RESTORE database
------------------


CREATE database fieldsense;

mysql -u root -p fieldsense < fieldsense_fieldsensestats_db.sql




------------------------------------------------------------------------------




				MULTI JOIN 
			--------------------------




 SELECT c.customer_name, a.appointment_time, a.appointment_end_time,p.purpose  FROM customers as c  INNER JOIN appointments as a  ON a.customer_id_fk=c.id INNER JOIN fieldsense.users as u ON a.user_id_fk= u.id  INNER JOIN activity_purpose as p ON a.purpose_id_fk= p.id  WHERE a.appointment_time="2018-03-14 12:19:00" AND a.appointment_end_time="2018-03-14 01:19:00" AND  c.record_state !=3 \G



SELECT c.customer_name, a.appointment_time, a.appointment_end_time,p.purpose, a.assigned_id_fk  FROM appointments a INNER JOIN customers c ON a.customer_id_fk=c.id INNER JOIN fieldsense.users as u ON a.user_id_fk= u.id  INNER JOIN activity_purpose as p ON a.purpose_id_fk= p.id  WHERE (appointment_end_time >="2018-03-14 01:19:00" AND appointment_time <= "2018-03-14 12:19:00" )  AND assigned_id_fk=61 and status !=2 and status !=3 AND a.record_state !=3;

