# -*- coding: utf-8 -*-
"""
Assignment 2.

ASU, SER 501
October 4th, 2016
Christopher Henderson
"""
from __future__ import division, print_function
from numpy import asarray, zeros, random, dot
from itertools import combinations

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
    sub_arrays = combinations(range(len(A)), 2)
    max_subarray = [0, 0]
    max_sum = 0
    for sub_array in sub_arrays:
        this_sum = sum(A[sub_array[0]:sub_array[1] + 1])
        if this_sum >= max_sum:
            max_subarray[0], max_subarray[1] = sub_array[0], sub_array[1]
            max_sum = this_sum
    this_sum = A[len(A) - 1]
    if this_sum >= max_sum:
        max_subarray[0], max_subarray[1] = len(A) - 1, len(A) - 1
        max_sum = this_sum
    return max_subarray[0], max_subarray[1], max_sum


def find_maximum_crossing_subarray(A, low, mid,  high):
    """

    Find the maximum subarray that crosses mid.

    Return a tuple (i,j) where A[i:j] is the maximum subarray.

    """
    mL = mR = None
    mE = li = ri = 0
    for index in range(mid, low - 1, -1):
        mE += A[index]
        mL = mL if mL is not None else mE
        if mE >= mL:
            mL = mE
            li = index
    mE = 0
    for index in range(mid + 1, high + 1):
        mE += A[index]
        mR = mR if mR is not None else mE
        if mE >= mR:
            mR = mE
            ri = index
    return li, ri, mR + mL


def find_maximum_subarray_recursive(A, low=0, high=-1):
    """

    Return a tuple (i,j) where A[i:j] is the maximum subarray.

    Recursive method from chapter 4

    """
    high = len(A) - 1 if high is -1 else high
    if low >= high:
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
        return (ci, cj, cs)


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
            mEij[0], mEij[1] = i + 1, i
        if mE >= mS:
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
    A11, A12, A21, A22 = split_into_quadrants(A)
    B11, B12, B21, B22 = split_into_quadrants(B)
    C11, C12, C21, C22 = split_into_quadrants(C)
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
    if len(A[0]) is 1:
        return A[0][0] * B[0][0]
    C = zeros(A.shape)
    A11, A12, A21, A22 = split_into_quadrants(A)
    B11, B12, B21, B22 = split_into_quadrants(B)
    C11, C12, C21, C22 = split_into_quadrants(C)
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
    C11[::, ::] = P5 + P4 - P2 + P6
    C12[::, ::] = P1 + P2
    C21[::, ::] = P3 + P4
    C22[::, ::] = P5 + P1 - P3 - P7
    return C


def split_into_quadrants(m):
    mid = m.shape[0] // 2
    return m[:mid:, :mid:], m[:mid:, mid:], m[mid:, :mid], m[mid:, mid:]


def test():
    """Test function."""
    arr = STOCK_PRICE_CHANGES
    for _ in range(100):
        arr = [random.randint(-100, 1000) for _ in range(100)]
        brute = find_maximum_subarray_brute(arr)
        recursive = find_maximum_subarray_recursive(arr)
        iterative = find_maximum_subarray_iterative(arr)
        brute_sum = sum(arr[brute[0]: brute[1] + 1])
        recursive_sum = sum(arr[recursive[0]: recursive[1] + 1])
        iterative_sum = sum(arr[iterative[0]: iterative[1] + 1])
        try:
            # We want to test the externally visible sums are the same.
            assert brute_sum == recursive_sum and recursive_sum == iterative_sum
        except:
            print(brute, recursive, iterative)
            print(arr)
            continue
    for _ in range(100):
        n = random.randint(1, 5)
        A = random.randint(0, 1000, (2**n, 2**n))
        B = random.randint(0, 1000, (2**n, 2**n))
        recursive = square_matrix_multiply(A, B)
        strassen = square_matrix_multiply_strassens(A, B)
        real = dot(A, B)
        assert ((recursive == real).all() and (strassen == real).all())


if __name__ == '__main__':
    test()
