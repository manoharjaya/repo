>start-hbase.sh

>hbase shell

--------------------------------------------------------------------------------------------------------------                               					create 'user','per','prof'

										put 'user','u-001','prof:degree','M.S.'
										put 'user','u-001','per:lname','Jaya'


										scan 'user'

										

-------------------------------------------------------------------------------------------------------------

								
								create 'customer','cust_per','cust_prof','cust_other'


								     put 'customer','cust_001','cust_per:f_name','Manohar'
									 put 'customer','cust_002','cust_per:f_name','Jaya'
									 put 'customer','cust_003','cust_per:f_name','lakshman'
									 put 'customer','cust_004','cust_per:f_name','ram'
									 put 'customer','cust_005','cust_per:f_name','ravi'
									 put 'customer','cust_006','cust_per:f_name','shekhar'
								 
								 

								 	 put 'customer','cust_007','cust_prof:real_name','Manohar jaya 01'
								 	 put 'customer','cust_008','cust_prof:real_name','jaya Manohar'
								 	 

								 	 get 'customer','cust_008' 

								 	 scan 'customer'


------------------------------------------------------------------------------------------------------------


