import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix = np.array(matrix)
	det = np.linalg.det(matrix)
	tr = np.trace(np.array(matrix))
	one, two = (tr + np.sqrt((tr ** 2) - (4 * det))) / (2.0), (tr - np.sqrt((tr ** 2) - (4 * det))) / (2.0)

	ans = [one]
	if (two != ans[-1]):
		ans.append(two)
	return list(sorted(ans))[::-1]
