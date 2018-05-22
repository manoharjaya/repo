import tensorflow as tf
# g=tf.Graph()
# with g.as_default():
with tf.Graph().as_default():

	v1=tf.constant([1,2,3,4,5,6],dtype=tf.int32)

	v2=tf.ones([6],dtype=tf.int32)

	sum=tf.add(v1,v2,name='add')

	with tf.Session() as sess:
		print 'v1=',v1.eval()
		print 'v2=',v2.eval()
		print 'sum=',sum.eval()

