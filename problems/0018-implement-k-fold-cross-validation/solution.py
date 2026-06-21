import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    tt: Tuple[List[int], List[int]] = []

    shuf = np.arange(n_samples)
    s = set([x for x in range(n_samples)])
    if (shuffle):
        np.random.shuffle(shuf)
    
    split = np.array_split(shuf, k)
    for i in range(len(split)):
        diff = np.concatenate([split[j] for j in range(k) if i != j])
        tt.append((diff.tolist(), split[i].tolist()))
    return tt