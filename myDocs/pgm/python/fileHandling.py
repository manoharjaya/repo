
# file write 

fo=open("/home/manohar/demods.txt","wb") # by default is read mode 

fo.write("hello manohar march 11 ashwin")  # overwrites existing data

fo.close()




#file read


fo=open("/home/manohar/demods.txt") # by default is read mode 

readString= fo.read(15);  # arg is byte values

print readString


print fo.tell()  # it tells you current postion of file pointer 


fo.seek(5, 0); # seek(offset,from )  


# The seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved.

# If from is set to 0, it means use the beginning of the file as the reference position and 1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position. 

readString= fo.read(15);  # arg is byte values

print readString

import os

os.rename("/home/manohar/demods.txt","/home/manohar/manobyFile.txt")


# Delete file manobyFile.txt
os.remove("/home/manohar/manobyFile.txt")


#rmdir
os.rmdir("/home/manohar/manobyFile")
# mkdir 
os.mkdir("/home/manohar/manobyFile")


class MyClass(object):
    def meth_a(self):
        pass  #Suppose you are designing a new class with some methods that you don't want to implement, yet.


    def meth_b(self):
        print "I'm meth_b"





