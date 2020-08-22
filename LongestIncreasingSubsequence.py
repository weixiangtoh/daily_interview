"""
You are given an array of integers. 
Return the length of the longest increasing subsequence (not necessarily contiguous) in the array.

Example:
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
"""
def longestSubsequence(nums):
    # pointer = 0
    # prev = 0
    # result = []
    # subseq = [nums[0]]
    # while pointer < len(nums) -1:
    #     pointer += 1
    #     if nums[pointer] > nums[prev]:
    #         subseq.append(nums[pointer])
    #         prev += 1
    #     else:
    #         result.append(subseq)
    #         subseq = [nums[pointer]]
    #         prev = pointer
    return result

if __name__ == "__main__":
    print(longestSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))