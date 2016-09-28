# -*- coding: utf-8 -*-from __future__ import division
from numpy import *from itertools import combinations_with_replacement

# STOCK_PRICES  = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22,                    15, -4, 7]def find_maximum_subarray_brute(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Implement the brute force method from chapter 4
    time complexity = O(n^2)
    """    # combinations_with_replacement(range(len(A)), 2) builds all subarray    # indices.    # E.G. [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2), (1, 3),    #       (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]    # Such that we can iterate over those and select the maximum sum of A
    # using these indices.    sub_arrays = combinations_with_replacement(range(len(A)), 2)
    max_subarray = (0, 0)
    max_sum = 0
    for sub_array in sub_arrays:
        this_sum = sum(A[sub_array[0]:sub_array[1] + 1])
        if this_sum > max_sum:
            max_subarray = sub_array
            max_sum = this_sum
    return max_subarray
print(find_maximum_subarray_brute([1,2,3,-3,2]))


#Implement pseudocode from the book
def find_maximum_crossing_subarray(A, low, mid,  high):
    """
    Find the maximum subarray that crosses mid
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    """    mE = mL = mR = 0
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
    """    high = len(A) - 1 if high is -1 else high
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
        return (ci, cj, cs)



def find_maximum_subarray_iterative(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Do problem 4.1-5 from the book.
    """    mS = mE = 0
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
    return mSij

# print (find_maximum_subarray_iterative([1,2,3,-5,2]))

def square_matrix_multiply(A, B):
    """
    Return the product AB of matrix multiplication.
    """
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape

    #TODO


def square_matrix_multiply_strassens(A, B):
    """
    Return the product AB of matrix multiplication.
    Assume len(A) is a power of 2
    """
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    assert (len(A) & (len(A) -1)) == 0, "A is not a power of 2"
    #TODO
    pass


def test():
    #TODO: Test all of the methods and print results.
    pass


if __name__ == '__main__':
    test()