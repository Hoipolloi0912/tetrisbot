import numpy as np
import random

class NeuralNetwork():
    def __init__(self, input_size, hidden_size, output_size, hidden_layers):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.hidden_layers = hidden_layers
        self.weights = []
        self.biases = []

        self.weights.append(np.random.randn(input_size,hidden_size))
        self.biases.append(np.zeros((1,hidden_size)))

        for _ in range(hidden_layers - 1):
            self.weights.append(np.random.randn(hidden_size, hidden_size))
            self.biases.append(np.zeros((1, hidden_size)))

        self.weights.append(np.random.randn(hidden_size, output_size))
        self.biases.append(np.zeros((1, output_size)))
    
    def forward(self, x):
        y = x
        #relu activation for middle layers
        for i in range(self.hidden_layers):
            y = np.maximum(0,np.dot(y ,self.weights[i]) + self.biases[i])
        y = np.dot(y, self.weights[-1]) + self.biases[-1]
        return y
    
    def mutate(self,mutation_rate):
        for i in range(len(self.weights)):
            if random.random() < mutation_rate:
                self.weights[i] += np.random.randn(*self.weights[i].shape) * mutation_rate
                self.biases[i] += np.random.randn(*self.biases[i].shape) * mutation_rate