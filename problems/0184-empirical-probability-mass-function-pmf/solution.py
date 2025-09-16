import numpy as np

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    lsamp = len(samples)
    samples = np.array(samples)
    distinct = np.unique(samples)
    dist = [(distinct[i], (np.sum(samples == distinct[i]) / lsamp)) for i in range(distinct.shape[0])]
    return dist
