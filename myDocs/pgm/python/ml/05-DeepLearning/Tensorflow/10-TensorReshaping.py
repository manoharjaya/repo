import tensorflow as tf
with tf.Graph().as_default(), tf.Session() as sess:
  # Task: Reshape two tensors in order to multiply them
  
  # Here are the original operands, which are incompatible
  # for matrix multiplication:
  a = tf.constant([5, 3, 2, 7, 1, 4])
  b = tf.constant([4, 6, 3])
  # We need to reshape at least one of these operands so that
  # the number of columns in the first operand equals the number
  # of rows in the second operand.

  # Reshape vector "a" into a 2-D 2x3 matrix:
  reshaped_a = tf.reshape(a, [2,3])

  # Reshape vector "b" into a 2-D 3x1 matrix:
  reshaped_b = tf.reshape(b, [3,1])

  # The number of columns in the first matrix now equals
  # the number of rows in the second matrix. Therefore, you
  # can matrix mutiply the two operands.
  c = tf.matmul(reshaped_a, reshaped_b)
  print(c.eval())

  # An alternate approach: [6,1] x [1, 3] -> [6,3]
