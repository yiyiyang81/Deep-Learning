import tensorflow as tf
import numpy as np


def load_cifar10():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    x_train = x_train.astype(np.float32) / 255.0
    x_test = x_test.astype(np.float32) / 255.0
    y_train = y_train.astype(np.int32)
    y_test = y_test.astype(np.int32)
    return (x_train, y_train), (x_test, y_test)
