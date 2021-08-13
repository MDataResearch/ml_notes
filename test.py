import numpy as np
import tensorflow as tf

# a = np.array([[0, 1], [1, 0]])
# b = np.array([[1, 2], [3, 4]])
# c = np.int64(a > 0)
# d = np.multiply(b, c)

# print(a)
# print(b)
# print(a > 0)
# print(c)
# print(d)

# If you want to be specific, you can set the dtype (see below) at creation time
rank_2_tensor = tf.constant([[1, 2],
                             [3, 4],
                             [5, 6]], dtype=tf.float16)
print(rank_2_tensor)