from __future__ import division

# def max_subarray(A, i=0, j=-1):
#     j = len(A) - 1 if j is -1 else j
#     if i == j:
#         return A[i]
#     mid = (i + j) // 2
#     max_left = max_subarray(A, i, mid)
#     max_right = max_subarray(A, mid + 1, j)
#     max_crossing = max_crossing_array(A, i, mid, j)
#     return max(max_left, max_right, max_crossing)
#
# def max_crossing_array(A, i, mid, j):
#     mE = mL = mR = 0
#     for v in A[mid::-1]:
#         mE += v
#         mL = max(mL, mE)
#     mE = 0
#     for v in A[mid+1::]:
#         mE += v
#         mR = max(mR, mE)
#     return mR + mL


def max_subarray(A, i=0, j=-1):
    j = len(A) - 1 if j is -1 else j
    if i == j:
        return i, i, A[i]
    mid = (i + j) // 2
    li, lj, ls = max_subarray(A, i, mid)
    ri, rj, rs = max_subarray(A, mid + 1, j)
    ci, cj, cs = max_crossing_array(A, i, mid, j)
    if ls >= rs and ls >= cs:
        return (li, lj, ls)
    if rs >= ls and rs >= cs:
        return (ri, rj, rs)
    if cs >= ls and cs >= rs:
        return (ci, cj, cs)

def max_crossing_array(A, i, mid, j):
    mE = mL = mR = 0
    li = ri = 0
    for index in range(mid, i - 1, -1):
        mE += A[index]
        if mE > mL:
            mL = mE
            li = index
    mE = 0
    for index in range(mid + 1, j + 1):
        mE += A[index]
        if mE > mR:
            mR = mE
            ri = index
    return li, ri, mR + mL


print (max_subarray([1,2,3,-2,3]))
