import tensorflow as tf

# Create a graph.
g = tf.Graph()

# Establish the graph as the "default" graph.
with g.as_default():
  # Assemble a graph consisting of the following three operations:
  #   * Two tf.constant operations to create the operands.
  #   * One tf.add operation to add the two operands.
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  z= tf.constant(4,name='z')
  my_sum = tf.add(x, y,name="x_y_z_sum")

  my_sum1 = tf.add(my_sum,z,name="x_y_z_sum")


  # Now create a session.
  # The session will run the default graph.
  with tf.Session() as sess:
    print my_sum1.eval()
