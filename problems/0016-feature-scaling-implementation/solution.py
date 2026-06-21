import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	m, s = np.mean(data, axis=0), np.std(data, axis=0)
	mn, mx = np.min(data, axis=0), np.max(data, axis=0)
	s = np.where(s == 0, 1, s)
	div = np.where(mx == mn, 1, mx - mn)
	
	standardized_data = (data - m) / s
	normalized_data = (data - mn) / div

	return (standardized_data, normalized_data)