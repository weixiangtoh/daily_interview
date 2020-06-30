"""
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
Here's the function signature:

def singleNumber(nums):
  # Fill this in.

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1

Challenge: Find a way to do this using O(1) memory.
"""

def singleNumber(nums):
    # Fill this in.
    num_dict = {}
    for element in nums:
        if element not in num_dict:
            num_dict[element] = 1
        else:
            num_dict[element] += 1

    output = []
    for key, value in num_dict.items():
        if value == 1:
            output.append(key)
    
    return output

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# [1]
print(singleNumber([4, 9, 2, 4, 7, 9, 2]))
# [7]
print(singleNumber([0, 4, 3, 2, 7, 8, 2, 3, 1]))
# [0, 4, 7, 8, 1]