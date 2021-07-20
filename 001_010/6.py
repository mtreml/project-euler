import numpy as np
import time


def sum_of_squares(N):

    return np.sum(np.arange(1, N+1)**2)


def square_of_sum(N):

    return np.arange(1, N+1).sum()**2


def result(N):

    return square_of_sum(N) - sum_of_squares(N)


def loop_result(N):
    """
    after simplifying:

    sum i*j for i < j
    """

    s = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if i < j:
                s += i*j

    return 2*s


def result1(N):
    """
    after simplifying:

    sum i*j for i < j
    """

    a = np.arange(1, N+1)
    A = np.einsum('i,j', a, a)

    return A.sum() - np.diag(A).sum()


N = 100

t0 = time.time()
print(result(N))
print(time.time() - t0)

t0 = time.time()
print(loop_result(N))
print(time.time() - t0)

t0 = time.time()
print(result1(N))
print(time.time() - t0)
