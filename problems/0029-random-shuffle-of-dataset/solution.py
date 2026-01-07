import numpy as np
import random

def shuffle_data(X, y, seed=None):	
	Xlist = X.tolist()
	ylist = y.tolist()

	data = None
	for (x, y) in zip(Xlist, ylist):
		x = np.append(x, y)
		if data is None:
			data = x
		else:
			data = np.vstack((data, x))

	np.random.seed(seed)
	np.random.shuffle(data)

	Xprime = None
	yprime = []
	for i in range(data.shape[0]):
		content = data[i, 0:-1]
		value = data[i, -1]
		if Xprime is None:
			Xprime = content
		else:
			Xprime = np.vstack((Xprime, content,))
		yprime.append(value)
	
	return Xprime, np.array(yprime)