# -*- coding: utf-8 -*-
from numpy import *

# TODO: Replace all TODO comments (yes, this one too!)



#STOCK_PRICES  = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
STOCK_PRICE_CHANGES =[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]




#Implement pseudocode from the book
def find_maximum_subarray_brute(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Implement the brute force method from chapter 4
    time complexity = O(n^2)
    """
    #TODO



#Implement pseudocode from the book
def find_maximum_crossing_subarray(A, low, mid,  high):
    """
    Find the maximum subarray that crosses mid
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    """
    #TODO



def find_maximum_subarray_recursive(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Recursive method from chapter 4
    """
    #TODO


def find_maximum_subarray_iterative(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Do problem 4.1-5 from the book.
    """    mS = mE = 0
    mSij = [0, 0]
    mEij = [0, 0]
    for i, v in enumerate(A):
        tmpME = mE + v
        print ("top",mSij)
        if tmpME > 0:
            mE = tmpME
            mEij[1] = i
        else:
            mE = 0
            mEij[0], mEij[1] = i, i
        if mE > mS:
            mS = mE
            mSij[0], mSij[1] = mEij[0], mEij[1]
    return mSij,mS

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