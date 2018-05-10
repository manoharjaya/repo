import tensorflow as tf

'''

With tensor addition and matrix multiplication each imposing constraints on operands, TensorFlow programmers must frequently reshape tensors.

You can use the tf.reshape method to reshape a tensor. For example, you can reshape a 8x2 tensor into a 2x8 tensor or a 4x4 tensor:
'''
with tf.Graph().as_default():
  # Create an 8x2 matrix (2-D tensor).
  matrix = tf.constant([[1,2], [3,4], [5,6], [7,8],
                        [9,10], [11,12], [13, 14], [15,16]], dtype=tf.int32)

  # Reshape the 8x2 matrix into a 2x8 matrix.
  reshaped_2x8_matrix = tf.reshape(matrix, [2,8])
  
  # Reshape the 8x2 matrix into a 4x4 matrix
  reshaped_4x4_matrix = tf.reshape(matrix, [4,4])

  with tf.Session() as sess:
    print "Original matrix (8x2):"
    print matrix.eval()
    print "Reshaped matrix (2x8):"
    print reshaped_2x8_matrix.eval()
    print "Reshaped matrix (4x4):"
    print reshaped_4x4_matrix.eval()
