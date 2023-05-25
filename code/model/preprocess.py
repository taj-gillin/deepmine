import numpy as np
from tensorflow.keras import datasets
import tensorflow as tf


def load_and_preprocess_data():
    '''This is where we load in and preprocess our data! We load in the data 
        for you but you'll need to flatten the images, normalize the values and 
        convert the input images from numpy arrays into tensors
    Return the preprocessed training and testing data and labels!'''
    
    # Load in the training and testing data from the MNIST dataset
    (train_inputs, train_labels), (test_inputs, test_labels) = datasets.mnist.load_data()

    train_inputs = train_inputs / 255
    test_inputs = test_inputs / 255

    train_inputs = np.reshape(train_inputs, (-1, 28, 28, 1))
    test_inputs = np.reshape(test_inputs, (-1, 28, 28, 1))

    train_inputs = tf.image.resize(train_inputs, (16, 16))
    test_inputs = tf.image.resize(test_inputs, (16, 16))

    train_inputs = np.round(train_inputs)
    test_inputs = np.round(test_inputs)


    # Convert labels to onehot
    train_labels = tf.one_hot(train_labels, 10)
    test_labels = tf.one_hot(test_labels, 10)


    return train_inputs, train_labels, test_inputs, test_labels
