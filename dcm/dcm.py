import os
import math
import gower
import logging
import numpy as np
import collections

import dcm.logger
from dcm.fast_mst import MST

logger = logging.getLogger('dcm')
DEBUG = os.environ.get("DCM_DEBUG", 0)

def F1(X, y):
    """
    Calculate Maximum Fisher's Discriminant Ratio (F1)
      - X: ndarray features
      - y: ndarray target
    """
    maxr = -math.inf
    index = -1
    X_classes = {}
    averages_classes = {}
    averages = np.average(X, axis=0)
    counter = collections.Counter(y)
    for c in counter.keys():
        X_classes[c] = X[y==c]
        averages_classes[c] = np.average(X_classes[c], axis=0)
    for i in range(X.shape[-1]):
        r = 0
        numerator = 0.0
        denominator = 0.0
        for c in counter.keys():
            X_c = X_classes[c]
            averages_c = averages_classes[c]
            m = (averages_c[i] - averages[i])**2
            numerator += counter[c] * m
            x = X_c[:, i]
            x = x - averages_c[i]
            x = x**2
            denominator += np.sum(x)
        if denominator > 0:
            r = numerator/denominator
            if r > maxr:
                maxr = r
                index = i
        if DEBUG:
            logger.debug("{} => numerator = {}, denominator = {}, r = {}".format(i, numerator, denominator, r))
    return index, 1 / (1 + maxr)


def N1(X, y, cat_features=[]):
    """
    Calculate Fraction of Borderline Points (N1)
      - X: ndarray features
      - y: ndarray target
      - cat_features: a boolean array that specifies categorical features
    """

    if len(cat_features) == 0:
        cat_features = np.zeros(X.shape[-1], dtype=bool)
    
    # Calculate Gower distance matrix
    distance_matrix = gower.gower_matrix(X, cat_features=cat_features)

    # Generate a Minimum Spanning Tree
    tree = MST(distance_matrix)
    sub = tree[y[tree[:, 0]] != y[tree[:, 1]]]
    vertices = np.unique(sub.flatten())
    return len(vertices) / X.shape[0]


def C12(X, y):
    """
    Calculate Entropy of Class Proportions (C1) and Imbalance Ratio (C2)
      - X: ndarray features
      - y: ndarray target
    """
    n = len(y)
    counter = collections.Counter(y)
    entroy = 0.0
    tmp_sum = 0.0
    for c in counter.keys():
        pc = counter[c] / n
        entroy += pc * math.log(pc)
        tmp_sum += counter[c] / (n - counter[c])
    C1 = 1 - (-entroy / math.log(len(counter)))
    IR = ((len(counter) - 1) / len(counter)) * tmp_sum
    C2 = 1 - (1 / IR)
    return C1, C2
