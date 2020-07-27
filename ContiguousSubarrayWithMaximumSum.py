"""
You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.

Here's a starting point:

def max_subarray_sum(arr):
  # Fill this in.

print max_subarray_sum([34, -50, 42, 14, -5, 86])
# 137
"""
def max_subarray_sum(arr):
    # Fill this in.
    max_sum = 0
    for i in range(len(arr)):
        current_sum = arr[i]
        for j in range(i+1, len(arr)):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
print(max_subarray_sum([34, -50, 42, 14, -5, 86, -40]))
# 137
