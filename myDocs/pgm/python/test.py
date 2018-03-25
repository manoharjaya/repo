import MySQLdb
import time
import welcome_module                           # IMPORT ENTIRE FUNTIONALITY IN  THE PKG
from name_module import Name_module                   #IMPORT PARTICULAR FUNTION USING FORM MODULE NAME 
#PRINT
print "manohar"
# LIST
l1=["mano","jaya","mumbai"]
print "using list<------------------------->you are in = ",l1[2]
# TUPLE
t1=("t1","t2","t3","t4")
print "using tuple<------------------------>you are in = ",t1
# DICTIONARY
dic={"name":"manohar","age":"22","designation":"Java Developer"}
# DICTIONARY VALUES
print dic.values()
# LENGTH
length=len(dic.values())
print "length=",length
#RANGE
ranges=range(2,10)
for each in ranges:
	print "ranges=",each
count=2
for e in range(1,20):
	print "2's table=",e*2
print("latest one using paranthesis")
# BREAK
for letter in "manohar":
	print letter
	if letter=="h":
		break 
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter
# MEMBERSHIP --------------------------------------------------------returns boolean
james="set"
print "e" in james
# ADD AND UPDATING THE DICTIONARY
dic["name"]="manohar jaya"
dic["project"]="free lance Hadoop"
print dic
print "Current time was=",time.localtime(time.time())

# -----------------------------------------------------------------------------

# DEFINING FUNCTION                   // THIS TAKE EXACTLY ONE ARGUMENTS
def callme(str):
	"this is string doc ,optional"
	print "callme method is called.."+str
	return
    
callme("welcome to python manohar..") # ATLEAST YOU HAVE TO PASS ONE ARG



# -------------------------------------------------------------------------------

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

# ------------------------------------------------------------------------------------


# KEYWORD ARGUMENTS



def keywordsArg(str):
	print str
	return
keywordsArg(str="keywordsArg is calling..")

def user_infomation(designation,name):            #ORDER DOESNOT MATTER  BUT NAME SHOULD MATCH
	print "name="+name,"designation=",designation
	return
user_infomation(name="manohar jaya",designation="data engineer")
 


 # ---------------------------------------------------------------------------------


# VARIABLE ARGUMENTS



def variable_Arg(a,*varArg):
	"variable_Arg"
	print "a=",a
	for eachArg in varArg:
		print "varArg=",eachArg
	return
variable_Arg(10)
variable_Arg(20,30,40)

welcome_module.Welcome_module()   #   import welcome_module  
Name_module()                     #   from name_module import Name_module    


# --------------------------------------INPUT---------------------------------------------
 

getValue=raw_input("Enter your Input..")
print "Entered Input is ",getValue

try:
	fw=open("write you.txt","a+")
	fw.write("hello manohar \n you are adding further txt")
	fw.close()
except Exception, e:
	raise e

# ---------------------------------------CLASS-------INHERITENCE--------------------------------------

class First(object):
		"""docstring for ClassName"""
		def __init__(self, arg):
			self.arg = arg
			print "one ARGUMENTS constructor is called..",arg
		def display(self,a):
			"display method"
			print "display method is called"
			print "a=%d"%a 
class Second(First):
		"""docstring for ClassName"""
		def __init__(self, arg):
			"constructor docstring"
			self.arg = arg
			print "Second class is called---------",arg
		def display2(self,b):
			"display2 docstring"
			print "Second display2 method is called------",b
s1=Second("DATA SCIENTIST..")
s1.display2("LEARN DATA STRUCTURE")
s1.display(752)

# -------------------------------------MYSQL   DB -------------------------------------------

                    # ----MUST USE import MySQLdb before using db connection---

db=MySQLdb.connect("localhost","root","root","test")   #create a db connection

cursor=db.cursor()           #make the cursor for accessing the Operation

sql="INSERT INTO customer (first_name,last_naem,address1,address2,country) VALUES('%s','%s','%s','%s','%s')"%("testoct 31","work hard","to learn","data structure","this month")

try:
	cursor.execute(sql)     #Execute the sql query
	db.commit()             
except Exception, e:
	db.rollback()
	print "Mnaohar Error",e
db.close()


# ---------------------------------------------------------------------------------------------