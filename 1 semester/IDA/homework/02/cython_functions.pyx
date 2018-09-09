import numpy as np
cimport numpy as np
cimport cython

from libc.math cimport sqrt
from libc.math cimport pow
from libcpp cimport bool
from cpython cimport bool


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef matrix_multiply(np.ndarray[np.float64_t, ndim=2] X,
                      np.ndarray[np.float64_t, ndim=2] Y):
    """ Matrix multiplication
    Inputs:
      - X: A numpy array of shape (N, M)
      - Y: A numpy array of shape (M, K)
    Output:
      - out: A numpy array of shape (N, K)
    """
    cdef np.ndarray[np.float64_t, ndim=2] ans;
    ans = np.zeros((X.shape[0], Y.shape[1]))

    cdef np.float64_t tmp;
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            tmp = 0
            for k in range(X.shape[1]):
                tmp += X[i, k] * Y[k, j]
            ans[i, j] = tmp
    return ans


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef matrix_rowmean(np.ndarray[np.float64_t, ndim=2] X,
                     np.ndarray[np.float64_t, ndim=1] weights):
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
    cdef np.ndarray[np.float64_t, ndim=1] ans;
    ans = np.zeros(X.shape[0], dtype=np.float64)

    if weights.shape[0] == 0:
        weights = np.ones(X.shape[1], dtype=np.float64)

    cdef np.float64_t sum = 0.0;
    for i in range(weights.shape[0]):
        sum += weights[i]

    cdef np.float64_t const_div = 1. / sum;

    cdef np.float64_t tmp;
    for i in range(X.shape[0]):
        tmp = 0.0
        for j in range(X.shape[1]):
            tmp += X[i, j] * weights[j]
        ans[i] = tmp * const_div
    return ans


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef matrix_rowstd(np.ndarray[np.float64_t, ndim=2] X):
    cdef np.ndarray[np.float64_t, ndim=1] ans;
    ans = np.zeros(X.shape[0], dtype=np.float64)

    cdef np.ndarray[np.float64_t, ndim=1] mean;
    mean = matrix_rowmean(X, weights=np.empty(0));

    cdef np.float64_t tmp;
    for i in range(X.shape[0]):
        tmp = 0.0
        for j in range(X.shape[1]):
            tmp += pow(X[i, j] - mean[i], 2)
        ans[i] = sqrt(tmp / X.shape[1])
    return ans


cpdef argsort(np.ndarray[np.float64_t, ndim=1] arr):
    return np.argsort(arr)


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef row_sqrt(np.ndarray[np.float64_t, ndim=1] row):
    cpdef np.float64_t ans = 0.0;
    for i in range(row.shape[0]):
        ans += pow(row[i], 2)
    return sqrt(ans)


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef cosine_similarity(np.ndarray[np.float64_t, ndim=2] X, np.int32_t top_n=10,
                        bool with_mean=True, bool with_std=True):
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
    cdef np.ndarray[np.float64_t, ndim=2] A;
    A = X.copy()

    cdef np.ndarray[np.float64_t, ndim=1] mean;
    if with_mean == True:
        mean = matrix_rowmean(A, weights=np.empty(0))
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                A[i, j] -= mean[i]

    cdef np.ndarray[np.float64_t, ndim=1] std;
    if with_std == True:
        std = matrix_rowstd(A)
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                A[i, j] /= std[i]

    for i in range(A.shape[0]):
        for j in argsort(A[i])[:-top_n]:
            A[i, j] = 0

    cdef np.ndarray[np.float64_t, ndim=2] ans;
    ans = np.zeros((A.shape[0], A.shape[0]))

    cdef np.ndarray[np.float64_t, ndim=1] row_sqrts;
    row_sqrts = np.ndarray(A.shape[0])
    for i in range(A.shape[0]):
        row_sqrts[i] = row_sqrt(A[i])

    cdef np.float64_t tmp;
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            tmp = 0.0
            for k in range(A.shape[1]):
                tmp += A[i][k] * A[j][k]
            ans[i, j] = tmp / row_sqrts[i] / row_sqrts[j]

    return ans