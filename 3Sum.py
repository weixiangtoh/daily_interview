"""
Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) 
in nums such that a + b + c = 0. 
Note that there may not be any triplets that sum to zero in nums, 
and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]
Here's a starting point:

class Solution(object):
  def threeSum(self, nums):
    # Fill this in.

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
"""
class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        required = {}
        for n in nums:
            if n not in required:
                required[n] = 1
            else:
                required[n] += 1
        print(required)
        result = []
        pointer = 1
        # for i in range(len(nums)):
        #     stack = {}

        return

if __name__ == "__main__":
    # Test Program
    nums = [1, -2, 1, 0, 5]
    print(Solution().threeSum(nums))
    # [[-2, 1, 1]]