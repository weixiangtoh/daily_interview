"""
You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.

Here is the function signature:

def check(lst):
  # Fill this in.

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False

Can you find a solution in O(n) time?
"""

def check(lst):
    # Fill this in.
    p = None
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            if p is not None:
                return False
            p = i
    # conditions for True:
        # 1. when p is 0
        # 2. when the array itself is alr non-decreasing --> p == none
    # corner cases:
        # 1. 2nd last index at len(lst) -2
        # 2. if length of array passed is longer than 3 
        # ---> we can change lst[p] to between lst[p-1] and lst[p+1]
        # ---> or lst[p+1] to between lst[p] and lst[p+2]
    if (p == 0) or (p == None) or (p == len(lst) - 2) or (lst[p] <= lst[p+1]) or (lst[p] <= lst[p+2]):
        return True
    return False

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False