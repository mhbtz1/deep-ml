import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros((A.shape[1], 1))
	diag_values = np.expand_dims(np.diag(A), axis=1)	
	diag = np.diag(np.diag(A))
	Adiff = A - diag

	b = np.expand_dims(b, axis=1)
	for _ in range(n):
		sub = b - Adiff @ x
		x = np.divide(sub, diag_values) 
	
	x = x.flatten().tolist()
	return list(map(lambda y: round(y, 4), x))