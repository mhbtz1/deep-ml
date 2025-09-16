import numpy as np


def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	means = []
	for v in vectors:
		mean = np.mean(v, axis=0)
		means.append(mean)
	
	res = np.empty((len(vectors), len(vectors),))
	for i in range(len(vectors)):
		for j in range(len(vectors)):
			m1, m2 = means[i], means[j]
			s1 = sum([(vectors[i][k] - m1) * (vectors[j][k] - m2) for k in range(len(vectors[i]))]) / (len(vectors[i]) - 1)
			res[i, j] = s1

	return res.tolist()

			