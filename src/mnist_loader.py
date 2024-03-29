import pickle
import gzip
import numpy as np

'''training_data is tuples of 50 000pcs MNIST data. First tuple value contains
MNIST training images and second tuple value is the digit value (0-9) of
corresponding image. Each image is a numpy ndarray with 784 values (28 x 28 pixels).

validation_data and test_data are similar to training_data, but contains only
10 000images each.'''

def load_data():
    #opening gzip-compressed file in binary read mode
    gzip_file = gzip.open('mnist.pkl.gz', 'rb')

    #deserialize the data from the file with pickel
    training_data, validation_data, test_data = pickle.load(gzip_file, encoding="latin1")
    gzip_file.close()

    return (training_data, validation_data, test_data)


def prepare_data():
    training_data, validation_data, test_data = load_data()

    #first tuple element image is 784-dimensional NumPy array representing images
    training_inputs = [np.reshape(image, (784, 1)) for image in training_data[0]]
    validation_inputs = [np.reshape(image, (784, 1)) for image in validation_data[0]]
    test_inputs = [np.reshape(image, (784, 1)) for image in test_data[0]]

    #second tuple element label is 10-dimensional NumPy array i.e. image digit value
    training_results = [label_to_vector(label) for label in training_data[1]]
    training_data = zip(training_inputs, training_results)

    #second tuple element label is an integer i.e. image digit value
    validation_data = zip(validation_inputs, validation_data[1])
    test_data = zip(test_inputs, test_data[1])

    return (training_data, validation_data, test_data)

#unit vector to describe right digit in vector from i.e. certain index 1.0 and other indexes 0 is digit=index
def label_to_vector(digit):
    label_vector = np.zeros((10, 1))
    label_vector[digit] = 1.0
    return label_vector