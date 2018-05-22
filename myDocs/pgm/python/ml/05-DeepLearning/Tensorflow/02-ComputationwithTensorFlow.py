import tensorflow as tf
# sess = tf.Session()
a = tf.constant(10)
b = tf.constant(32)
c=tf.add(a,b)
with tf.Session() as sess:
	print(sess.run(a+b))
	print sess.run(c)
	print c.eval()