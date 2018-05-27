# coding: utf-8

# ## Import dependencies
import os
import subprocess
import numpy as np
from glob import glob
from keras.preprocessing.image import *
from model import CNN_model



#print('Connect your smartphone to this system, mount your Internal Storage and note the absolute path of WhatsApp folder')
#print('For example: "/run/user/1000/gvfs/mtp:host=%5Busb%3A003%2C002%5D/Internal storage/WhatsApp" (without quotes) \n')
#WA_path = input('Enter absolute path of WhatsApp folder: \n')

WA_img_path ='/home/manohar/Desktop/test/'
WA_img_path.replace('//', '/') # shit happens
WA_img_path.replace(' ', '\\ ') # replace spaces with their escaped versions

# define model
model = CNN_model()
# load trained weights
model.load_weights('weights.h5')

others_path = WA_img_path + 'others/'

if 'notes'or'others' not in (os.path.exists(others_path),os.path.exists(others_path)):
	os.mkdir(others_path)
	os.mkdir(WA_img_path+'notes/')

'''

dir=[ x for x in os.listdir(WA_img_path)]
print 'dir=',dir

if dir.length!=0:
     for x in dir:
	print 'deleteDir=',x
	if x=='notes':
		print 'inside'
		#os.rmdir(WA_img_path)
	        subprocess.Popen(['rm', '-rf',notes_path])
		break

os.mkdir(notes_path)
'''

print('<------------------------------------------------------------------------------------------------->')
print('Created a "notes" And "others" folder in your TEST folder to keep the notes and other stuff')

def predict(file_path):
    '''
    predict whether file is a notes image
    '''
    #print 'call'
    img = load_img(file_path, target_size=(124, 124, 3))
    x = img_to_array(img) / 255. 
    y = model.predict(np.expand_dims(x, axis=0))
    return np.squeeze(y) > 0.5


# get file paths 
files = glob(WA_img_path + '*.*') + glob(WA_img_path + 'check/*.*') # print list of values

#print 'files=-----',files

# extract notes from WhatsApp Images folder

othersCount=0
notesCount=0
totalCount=0
print 'Total file present in check folder=',len(files)
for count, file_path in enumerate(files):
	totalCount+=1
        if not count % 10: print(str(count) + ' files examined')
        #print 'file_path=','\t',file_path
        if predict(file_path): # check if the file is one of the notes
		#print 'pre=',file_path
		file_name = file_path.split('/')[-1] # get file name
		#print 'file_name=',others_path+file_name
		os.rename(file_path,others_path+file_name) # move the file to 'notes' folder
		#copyfile(file_name,notes_path)
		#print 'file_name=',file_name
	
		othersCount+=1
		
        else:
		file_name = file_path.split('/')[-1] # get file name
		os.rename(file_path,WA_img_path+'notes/'+file_name)
		notesCount+=1
print 'Total files=',totalCount
print 'Notes files=',notesCount
print 'Other files=',othersCount

print('<------------------------------------------------------------------------------------------------->')

