"""
Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element can repeat.

Here is a starting point:

def findRanges(nums):
  # Fill this in.

print findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15])
# ['0->2', '5->5', '7->11', '15->15']
"""
def findRanges(nums):
    # Fill this in.
    prev = 0
    pointer = 1
    start = 0
    num_dict = {}
    while start < len(nums) and pointer < len(nums):
        if nums[pointer] - nums[prev] == 0 or nums[pointer] - nums[prev] == 1:
            prev += 1
        else:
            num_dict[nums[start]] = nums[prev]
            start = pointer
            prev = start

        if pointer == len(nums) -1:
            num_dict[nums[start]] = nums[prev]
    
        pointer += 1

    result = []
    for start, end in num_dict.items():
        item = str(start) + "->" + str(end)
        result.append(item)
    return result

print (findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']