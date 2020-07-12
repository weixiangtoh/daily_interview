"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Here is the method signature:

class Solution:
  def minSubArrayLen(self, nums, s):
    # Fill this in

print Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)
# 2
"""

class Solution:
    def minSubArrayLen(self, nums, s):
        # Fill this in

        # check last item in list
        if nums[-1] >= s:
            return 1
            
        min_len = len(nums)
        # cannot count the last item on the list as it will always return count = 1
        for i in range(len(nums)-1):
            total = 0
            count = 0
            for j in range(i, len(nums)):
                total += nums[j]
                count += 1
                if total >= s:
                    if count < min_len:
                        min_len = count
                    break

        return min_len


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 8))
# 3
print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 9))
# 3
print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 10))
# 4