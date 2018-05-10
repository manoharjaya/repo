'''
In linear algebra, when multiplying two matrices, the number of columns of the first matrix must equal the number of rows in the second matrix.

    It is valid to multiply a 3x4 matrix by a 4x2 matrix. This will result in a 3x2 matrix.
    It is invalid to multiply a 4x2 matrix by a 3x4 matrix.
'''

import tensorflow as tf

with tf.Graph().as_default():
  # Create a matrix (2-d tensor) with 3 rows and 4 columns.
  x = tf.constant([[5, 2, 4, 3], [5, 1, 6, -2], [-1, 3, -1, -2]],
                  dtype=tf.int32)

  # Create a matrix with 4 rows and 2 columns.
  y = tf.constant([[2, 2], [3, 5], [4, 5], [1, 6]], dtype=tf.int32)

  # Multiply `x` by `y`. 
  # The resulting matrix will have 3 rows and 2 columns.
  matrix_multiply_result = tf.matmul(x, y)

  with tf.Session() as sess:
    print matrix_multiply_result.eval()
