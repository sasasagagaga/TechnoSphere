from numba import jit
import numpy as np
from math import sqrt

@jit(nopython=True)
def matrix_multiply(X, Y):
    """ Matrix multiplication
    Inputs:
      - X: A numpy array of shape (N, M)
      - Y: A numpy array of shape (M, K)
    Output:
      - out: A numpy array of shape (N, K)
    """
    ans = np.zeros((X.shape[0], Y.shape[1]))

    for i in xrange(X.shape[0]):
        for j in xrange(Y.shape[1]):
            for k in xrange(X.shape[1]):
                ans[i, j] += X[i, k] * Y[k, j]

    return ans


@jit(nopython=True)
def matrix_rowmean(X, weights=np.empty(0)):
    """ Calculate mean of each row.
    In case of weights do weighted mean.
    For example, for matrix [[1, 2, 3]] and weights [0, 1, 2]
    weighted mean equals 2.6666 (while ordinary mean equals 2)
    Inputs:
      - X: A numpy array of shape (N, M)
      - weights: A numpy array of shape (M,)
    Output:
      - out: A numpy array of shape (N,)
    """
    ans = np.zeros(X.shape[0])
    if weights.size == 0:
        weights = np.ones(X.shape[1])

    sum = 0
    for w in weights:
        sum += w

    for i in xrange(X.shape[0]):
        for j in xrange(X.shape[1]):
            ans[i] += X[i, j] * weights[j]
        ans[i] /= sum

    return ans


@jit(nopython=True)
def matrix_rowstd(X):
    ans = np.zeros(X.shape[0])

    mean = matrix_rowmean(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            ans[i] += (X[i, j] - mean[i]) ** 2
        ans[i] = sqrt(ans[i] / X.shape[1])

    return ans


@jit(nopython=True)
def argsort(arr):
    return np.argsort(arr)


@jit(nopython=True)
def row_sqrt(row):
    ans = 0
    for r in row:
        ans += r ** 2
    return sqrt(ans)


@jit(nopython=True)
def cosine_similarity(X, top_n=10, with_mean=True, with_std=True):
    """ Calculate cosine similarity between each pair of row.
    1. In case of with_mean: subtract mean of each row from row
    2. In case of with_std: divide each row on it's std
    3. Select top_n best elements in each row or set other to zero.
    4. Compute cosine similarity between each pair of rows.
    Inputs:
      - X: A numpy array of shape (N, M)
      - top_n: int, number of best elements in each row
      - with_mean: bool, in case of subtracting each row's mean
      - with_std: bool, in case of subtracting each row's std
    Output:
      - out: A numpy array of shape (N, N)

    Example (with top_n=1, with_mean=True, with_std=True):
        X = array([[1, 2], [4, 3]])
        after mean and std transform:
        X = array([[-1.,  1.], [ 1., -1.]])
        after top n choice
        X = array([[0.,  1.], [ 1., 0]])
        cosine similarity:
        X = array([[ 1.,  0.], [ 0.,  1.]])

    """
    A = X.copy()

    if with_mean:
        mean = matrix_rowmean(A)
        for i in xrange(A.shape[0]):
            for j in xrange(A.shape[1]):
                A[i, j] -= mean[i]

    if with_std:
        std = matrix_rowstd(A)
        for i in xrange(A.shape[0]):
            for j in xrange(A.shape[1]):
                A[i, j] /= std[i]

    for i in xrange(A.shape[0]):
        for j in argsort(A[i])[:-top_n]:
            A[i, j] = 0

    row_sqrts = np.array(A.shape[0])
    for i in xrange(A.shape[0]):
        row_sqrts[i] = row_sqrt(A[i])

    ans = np.zeros((A.shape[0], A.shape[0]))
    for i in xrange(A.shape[0]):
        for j in xrange(A.shape[0]):
            for k in xrange(A.shape[1]):
                ans[i, j] += A[i][k] * A[j][k]
            ans[i, j] /= row_sqrts[i] * row_sqrts[j]

    return ans
