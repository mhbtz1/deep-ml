import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	matrix = np.array(matrix, dtype=np.float32)
    invmat = np.array([ [matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]], dtype=np.float32)

    det = (matrix[1, 1] * matrix[0, 0]) - (matrix[1, 0] * matrix[0, 1])
    return (1 / det) * invmat