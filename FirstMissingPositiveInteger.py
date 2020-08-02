"""
You are given an array of integers. 
Return the smallest positive integer that is not present in the array. 
The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.

Here's your starting point:

def first_missing_positive(nums):
  # Fill this in.

print first_missing_positive([3, 4, -1, 1])
# 2
"""
def first_missing_positive(nums):
    # Fill this in.
    if 1 not in set(nums):
        return 1
    
    min_value = 1
    for items in set(nums):
        if min_value == items:
            min_value += 1
        elif items != min_value and items != 0:
            return min_value


print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([3, 4, -1]))
print(first_missing_positive([-1, 0 , 2, 4, 5, 1]))
print(first_missing_positive([-1, 0 , 2, 4, 5, 3]))