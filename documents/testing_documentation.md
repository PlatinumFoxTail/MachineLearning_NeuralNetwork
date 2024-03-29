# Testing documentation

The testing focus of this project is set on the network (network.py), and not other parts such as the user interface (digit_predicter.ipynb). The testing can be divided into three parts: Sanity check, Prediction accuracy, and Unit testing & checkstyle. The last is self-explanatory, and the Sanity check includes a comparsion of intermediate outputs from the network and a simple network based on simplified input and output. Prediction accuracy visualizes the prediction accuracy of the neural network as a function of training epochs.

## Sanity check

### Description

In order to pressure test the network, a simple network was created for comparsion. The simple network (simple_network.py) had 3 neurons in the input layer, 4 neurons in the hidden layer, and 1 neuron in the output layer and no biases. The network, with the same neural network architecture as the simple network, and the simple network were fed with same simple input and output. The input was vectors with 3 elements either 0 or 1 values, and the output values were either 0 or 1. Since output values were chosen as either 0 or 1 values, 1 neuron in the output layer was sufficient. The learing rate was set to 0.01 for both the networks. The weights for both networks were also initialized with same random numbers.

The outputs from the neurons in the hidden layer and neuron the final layer was recorded during training for both the network and the simple network. The values were plotted for comparsion.

### Results

![Figure 1](https://github.com/PlatinumFoxTail/MachineLearning_NeuralNetwork/blob/main/images/070224.%20network%20vs.%20simple_network.%20eta%200.01%20no%20biases.png)

From the hidden layer outputs in the left-hand side graph in the figure above one can notice that, network's neurons 1&4 increases quite uniformly as a function of iterations while corresponding neurons of the simple network also increases but not as quickly. Further on the simple network's neurons 2&3 decrease quite uniformly as a function of iterations while corresponding neurons of the network also decreases, but not as quickly. Based on this observation it seems that network and the simple network hidden layer outputs correlates to each other, somehow "mirrored" e.g. when network's neuron's 1&4 increase uniformly the simple network's neurons 1&4 increase not as quickly and vice verca when simple network's neurons 2&3 decrease uniformly then network's neurons 2&3 decrease not as quickly. The "mirroring" should not be and issue, when testing the sanity of the network since same pair of neurons increases and decreases for both the netowork and the simple network.

More importantly it seems that, both networks output from output layer (right-hand side graph in figure above) approaches same value when iterations are sufficient. This gives more confidence that the network should be set up properly.

### Instructions to repeat test

1. In the network.py file, the biases and weights need to be uncommented on line 30-39 and commented out on lines 23-28. https://github.com/PlatinumFoxTail/MachineLearning_NeuralNetwork/blob/58606d727707a75be0624a31732c30e3411abfe9/src/network.py#L23-L39
2. Run benchmark_networks.py

## Prediction accuracy

The neural network predicts the handwritten digits with an accuracy of approx. 94%. In the graph below, it seems that ~94% prediction accuracy is reached already after 15 training epochs with 784 neurons in the input layer, 30 neurons in the hidden layer, 10 neurons in the output layer, 30 training epochs, mini-batch size 10, and learning rate 3.0 (obtained when running the training neural network block in digit_predicter.ipynb). Decent prediction accuracies are also achieved with few training epochs e.g. in the graph below already ~90% prediction accuracy after first trainig epoch. 

![Figure 1](https://github.com/PlatinumFoxTail/MachineLearning_NeuralNetwork/blob/main/images/010324.%20prediction%20accuracy%20per%20training%20epoch.png)

## Unit testing and checkstyle

![GHA workflow badge](https://github.com/PlatinumFoxTail/MachineLearning_NeuralNetwork/workflows/CI/badge.svg) 
[![codecov](https://codecov.io/gh/PlatinumFoxTail/MachineLearning_NeuralNetwork/graph/badge.svg?token=4JBGC70B3Z)](https://codecov.io/gh/PlatinumFoxTail/MachineLearning_NeuralNetwork)

For checkstyle pylint has been used. As of 1st of March the code has been rated as 8.86/10.
