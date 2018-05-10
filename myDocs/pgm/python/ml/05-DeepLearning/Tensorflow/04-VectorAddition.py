import tensorflow as tf

v1=tf.constant([1,2,3,4,5,6],dtype=tf.int32)

v2=tf.ones([6],dtype=tf.int32)

sum=tf.add(v1,v2,name='add')

with tf.Session() as sess:
	print sum.eval()

