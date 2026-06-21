import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	x1 = [ X[i:i+batch_size, :] for i in range(0, X.shape[0], batch_size)]
	if (y is None):
		t = [[x] for x in x1]
	else:
		y1 = [ y[i:i+batch_size] for i in range(0, y.shape[0], batch_size)]
		t = [ [x, y] for x, y in zip(x1, y1)]
	return t