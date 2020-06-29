"""
You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.

def two_sum(list, k):
  # Fill this in.

print two_sum([4,7,1,-3,2], 5)
# True

Try to do it in a single pass of the list.
"""
def two_sum(list, k):
  # Fill this in.
    required = {}
    for i in range(len(list)):
        # stores the items in array in the dictionary
        # key (element) : value (index)
        # if target num - the element is inside the dictionary alr, 
            # shows that the target can be reached!
            # working backwards!!!
        if k - list[i] in required:
            return True
        else:
            required[list[i]] = i

print(two_sum([4,7,1,-3,2], 5))
# True
print(two_sum([2,8,12,15], 20))
# True