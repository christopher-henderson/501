# -*- coding: utf-8 -*-
"""Assignment 2 ASU SER 501."""
from __future__ import division, print_function
from numpy import asarray, zeros, random, dot
from itertools import combinations_with_replacement

STOCK_PRICE_CHANGES = [
    13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def find_maximum_subarray_brute(A, low=0, high=-1):
    """
    Brutish max subarray solution.

    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Implement the brute force method from chapter 4
    time complexity = O(n^2)

    """
    # combinations_with_replacement(range(len(A)), 2) builds all subarray
    # indices.
    # E.G. [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2), (1, 3),
    #       (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
    # Such that we can iterate over those and select the maximum sum of A
    # using these indices.
    sub_arrays = combinations_with_replacement(range(len(A)), 2)
    max_subarray = [0, 0]
    max_sum = 0
    for sub_array in sub_arrays:
        this_sum = sum(A[sub_array[0]:sub_array[1] + 1])
        if this_sum > max_sum:
            max_subarray = list(sub_array)
            max_sum = this_sum
    return max_subarray[0], max_subarray[1], max_sum


def find_maximum_crossing_subarray(A, low, mid,  high):
    """

    Find the maximum subarray that crosses mid.

    Return a tuple (i,j) where A[i:j] is the maximum subarray.

    """
    mE = mL = mR = 0
    li = ri = 0
    for index in range(mid, low - 1, -1):
        mE += A[index]
        if mE > mL:
            mL = mE
            li = index
    mE = 0
    for index in range(mid + 1, high + 1):
        mE += A[index]
        if mE > mR:
            mR = mE
            ri = index
    return li, ri, mR + mL


def find_maximum_subarray_recursive(A, low=0, high=-1):
    """

    Return a tuple (i,j) where A[i:j] is the maximum subarray.

    Recursive method from chapter 4

    """
    high = len(A) - 1 if high is -1 else high
    if low == high:
        return low, low, A[low]
    mid = (low + high) // 2
    li, lj, ls = find_maximum_subarray_recursive(A, low, mid)
    ri, rj, rs = find_maximum_subarray_recursive(A, mid + 1, high)
    ci, cj, cs = find_maximum_crossing_subarray(A, low, mid, high)
    if ls >= rs and ls >= cs:
        return (li, lj, ls)
    if rs >= ls and rs >= cs:
        return (ri, rj, rs)
    if cs >= ls and cs >= rs:
        return ci, cj, cs


def find_maximum_subarray_iterative(A, low=0, high=-1):
    """

    Return a tuple (i,j) where A[i:j] is the maximum subarray.

    Do problem 4.1-5 from the book.

    """
    mS = mE = 0
    mSij = [0, 0]
    mEij = [0, 0]
    for i, v in enumerate(A):
        tmpME = mE + v
        if tmpME > 0:
            mE = tmpME
            mEij[1] = i
        else:
            mE = 0
            mEij[0], mEij[1] = i, i
        if mE > mS:
            mS = mE
            mSij[0], mSij[1] = mEij[0], mEij[1]
    return mSij[0], mSij[1], mS


def square_matrix_multiply(A, B):
    """Return the product AB of matrix multiplication."""
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    C = zeros(A.shape)
    if len(A[0]) is 1:
        return A[0][0] * B[0][0]
    mid = A.shape[1] // 2
    A11 = A[:mid:, :mid:]
    A12 = A[:mid:, mid:]
    A21 = A[mid:, :mid:]
    A22 = A[mid:, mid:]
    B11 = B[:mid:, :mid:]
    B12 = B[:mid:, mid:]
    B21 = B[mid:, :mid:]
    B22 = B[mid:, mid:]
    C11 = C[:mid:, :mid:]
    C12 = C[:mid:, mid:]
    C21 = C[mid:, :mid:]
    C22 = C[mid:, mid:]
    C11[::, ::] = square_matrix_multiply(A11, B11) + square_matrix_multiply(
                                        A12, B21)
    C12[::, ::] = square_matrix_multiply(A11, B12) + square_matrix_multiply(
                                        A12, B22)
    C21[::, ::] = square_matrix_multiply(A21, B11) + square_matrix_multiply(
                                        A22, B21)
    C22[::, ::] = square_matrix_multiply(A21, B12) + square_matrix_multiply(
                                        A22, B22)
    return C


def square_matrix_multiply_strassens(A, B):
    """

    Return the product AB of matrix multiplication.

    Assume len(A) is a power of 2

    """
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    assert (len(A) & (len(A) - 1)) == 0, "A is not a power of 2"
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    C = zeros(A.shape)
    if len(A[0]) is 1:
        return A[0][0] * B[0][0]
    mid = A.shape[1] // 2
    A11 = A[:mid:, :mid:]
    A12 = A[:mid:, mid:]
    A21 = A[mid:, :mid:]
    A22 = A[mid:, mid:]
    B11 = B[:mid:, :mid:]
    B12 = B[:mid:, mid:]
    B21 = B[mid:, :mid:]
    B22 = B[mid:, mid:]
    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12
    P1 = square_matrix_multiply_strassens(A11, S1)
    P2 = square_matrix_multiply_strassens(S2, B22)
    P3 = square_matrix_multiply_strassens(S3, B11)
    P4 = square_matrix_multiply_strassens(A22, S4)
    P5 = square_matrix_multiply_strassens(S5, S6)
    P6 = square_matrix_multiply_strassens(S7, S8)
    P7 = square_matrix_multiply_strassens(S9, S10)
    C = zeros(A.shape)
    C[:mid:, :mid:] = P5 + P4 - P2 + P6
    C[:mid:, mid:] = P1 + P2
    C[mid:, :mid] = P3 + P4
    C[mid:, mid:] = P5 + P1 - P3 - P7
    return C


def test():
    """Test function."""
    # arr = [1, 2, 3, -3, 2]
    # brute = find_maximum_subarray_brute(arr)
    # recursive = find_maximum_subarray_recursive(arr)
    # iterative = find_maximum_subarray_iterative(arr)
    # assert brute == recursive and recursive == iterative
    for _ in range(10):
        n = random.randint(1, 5)
        A = random.randint(0, 1000, (2**n, 2**n))
        B = random.randint(0, 1000, (2**n, 2**n))
        recursive = square_matrix_multiply(A, B)
        strassen = square_matrix_multiply_strassens(A, B)
        real = dot(A, B)
        assert ((recursive == real).all() and (strassen == real).all())


if __name__ == '__main__':
    test()
