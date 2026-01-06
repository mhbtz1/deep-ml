import math
import numpy as np

def sigmoid(x):
        return (1 / (1 + np.exp(-x)))

def mse(y_pred, y_output):
        N = y_pred.shape[1]
        diff = y_pred - y_output
        return (1 / (float)(N)) * ((diff) @ diff.T)

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
        # Your code here
        features = np.array(features)
        weights = np.expand_dims(np.array(weights),axis=1)
        labels = np.expand_dims(np.array(labels),axis=0)

        z_output = (features @ weights) + bias
        a_output = sigmoid(z_output).T # get row vector with transpose op
        mse_output = mse(a_output, labels)
        return np.round(a_output, 4).tolist(), round(mse_output.item(), 4)

