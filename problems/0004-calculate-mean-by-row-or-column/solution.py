import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    matrix = np.array(matrix)
    return (matrix.mean(axis=1) if mode == 'row' else matrix.mean(axis=0))