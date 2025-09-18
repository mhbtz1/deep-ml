import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
    m, n = X.shape
    theta = np.zeros((n, 1))
    y = np.expand_dims(y, axis=-1)

    for i in range(iterations):
        mul = X.T @ ( (X @ theta) - y)
        theta = theta - (alpha * (1 / m) * mul)

    return np.round(theta, decimals=4)