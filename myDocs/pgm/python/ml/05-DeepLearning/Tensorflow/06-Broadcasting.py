'''
In mathematics, you can only perform element-wise operations (e.g. add and equals) on tensors of the same shape. 
In TensorFlow, however, you may perform operations on tensors that would traditionally have been incompatible. 
TensorFlow supports broadcasting (a concept borrowed from numpy), 
where the smaller array in an element-wise operation is enlarged to have the same shape as the larger array. For example, via broadcasting:

    If an operand requires a size [6] tensor, a size [1] or a size [] tensor can serve as an operand.
    If an operation requires a size [4, 6] tensor, any of the following sizes can serve as an operand:
        [1, 6]
        [6]
        []
'''

import tensorflow as tf

with tf.Graph().as_default():
  # Create a six-element vector (1-D tensor).
  primes = tf.constant([1,2, 3, 4, 5, 6], dtype=tf.int32)

  # Create a constant scalar with value 1.
  ones = tf.constant(1, dtype=tf.int32)

  # Add the two tensors. The resulting tensor is a six-element vector.
  just_beyond_primes = tf.add(primes, ones)

  with tf.Session() as sess:
    print just_beyond_primes.eval()
    