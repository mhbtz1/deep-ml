import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	try:
		sinv = np.linalg.inv(S)
		return (np.linalg.inv(T) @ A) @ S
	except Exception:
		return -1