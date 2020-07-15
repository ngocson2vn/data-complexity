import numpy as np
import collections

VERSION = "0.0.4"

def F1(X, y):
    """
    Calculate Maximum Fisher's Discriminant Ratio (F1)
      - X: ndarray features
      - y: ndarray target
    """
    maxr = -1
    index = -1
    X_classes = {}
    averages_classes = {}
    averages = np.average(X, axis=0)
    counter = collections.Counter(y)
    for c in counter.keys():
        X_classes[c] = X[y==c]
        averages_classes[c] = np.average(X_classes[c], axis=0)
    for i in range(X.shape[-1]):
        numerator = 0
        denominator = 0
        for c in counter.keys():
            X_c = X_classes[c]
            averages_c = averages_classes[c]
            m = (averages_c[i] - averages[i])**2
            numerator += counter[c] * m
            x = X_c[:, i]
            x = x - averages_c[i]
            x = x**2
            denominator += np.sum(x)
        r = numerator/denominator
        if r > maxr:
            maxr = r
            index = i
    return index, 1 / (1 + maxr)