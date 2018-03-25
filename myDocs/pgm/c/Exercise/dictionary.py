print "dictionary"

dic={
	"name":"manohar",
	"age":23,
	"color":"black"	
}

inp = raw_input("Enter the key..")
print "value is=",dic.get(inp,-1)