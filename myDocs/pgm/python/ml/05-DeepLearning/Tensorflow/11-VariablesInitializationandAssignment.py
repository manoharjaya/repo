import tensorflow as tf

'''
So far, all the operations we performed were on static values (tf.constant); calling eval() always returned the same result.
TensorFlow allows you to define Variable objects, whose values can be changed.

When creating a variable, you can set an initial value explicitly, or you can use an initializer (like a distribution):
'''

g = tf.Graph()
with g.as_default():
  # Create a variable with the initial value 3.
  v = tf.Variable([3])
  shapeV=tf.shape(v)
  # Create a variable of shape [1], with a random initial value,
  # sampled from a normal distribution with mean 1 and standard deviation 0.35.
  w = tf.Variable(tf.random_normal([1], mean=1.0, stddev=0.35))


with g.as_default():
  with tf.Session() as sess:
    initialization = tf.global_variables_initializer()
    sess.run(initialization)
    # Now, variables can be accessed normally, and have values assigned to them.
    print v.eval()
    print w.eval()
    print 'shapeV=',shapeV

'''
To change the value of a variable, use the assign op. Note that simply creating the assign op will not have any effect.
 As with initialization, you have to run the assignment op to update the variable value:
'''
with g.as_default():
  with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # This should print the variable's initial value.
    print v.eval()

    assignment = tf.assign(v, [7])
    # The variable has not been changed yet!
    print v.eval()

    # Execute the assignment op.
    sess.run(assignment)
    # Now the variable is updated.
    print v.eval()

