import numpy as np


def get_threshold(scores):
    if len(scores) < 5:
        return 0.85

    mean = np.mean(scores)
    std = np.std(scores)

    return max(0.7, mean - std)
