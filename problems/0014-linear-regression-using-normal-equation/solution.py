import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	y = np.expand_dims(np.array(y), axis=1)
	X = np.array(X)

	theta =  np.linalg.inv(X.T @ X) @ (X.T @ y)
	return np.asarray(np.squeeze(theta, axis=1))