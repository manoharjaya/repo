'''
You can also use tf.reshape to change the number of dimensions (the "rank") of the tensor. 
For example, you could reshape that 8x2 tensor into a 3-D 2x2x4 tensor or a 1-D 16-element tensor.

'''
import tensorflow as tf

with tf.Graph().as_default():
  # Create an 8x2 matrix (2-D tensor).
  matrix = tf.constant([[1,2], [3,4], [5,6], [7,8],
                        [9,10], [11,12], [13, 14], [15,16]], dtype=tf.int32)

  # Reshape the 8x2 matrix into a 3-D 2x2x4 tensor.
  reshaped_2x2x4_tensor = tf.reshape(matrix, [2,2,4])
  
  # Reshape the 8x2 matrix into a 1-D 16-element tensor.
  one_dimensional_vector = tf.reshape(matrix, [16])

  with tf.Session() as sess:
    print "Original matrix (8x2):"
    print matrix.eval()
    print "Reshaped 3-D tensor (2x2x4):"
    print reshaped_2x2x4_tensor.eval()
    print "1-D vector:"
    print one_dimensional_vector.eval()
