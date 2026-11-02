import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    scores = np.array(scores)
    # e^x / sum(e^x) = e^(log(e^x / sum(e^x))) = e^(log(e^x) - log(sum(e^x)))
    x = np.exp(scores - np.max(scores))
    sm = np.sum(x).item()
    res = np.exp(np.log(x) - np.log(sm))
    return res.tolist()
    