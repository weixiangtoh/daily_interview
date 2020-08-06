"""
You are given a string s, and an integer k. 
Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

Here's a starting point:

def longest_substring_with_k_distinct_characters(s, k):
  # Fill this in.

print longest_substring_with_k_distinct_characters('aabcdefff', 3)
# 5 (because 'defff' has length 5 with 3 characters)
"""
def longest_substring_with_k_distinct_characters(s, k):
    # Fill this in.
    max_len = 0
    start = 0
    distinct = 0
    stack = []

    if len(s) < 1:
        return 0

    for end in range(len(s)):
        if s[end] not in stack:
            distinct += 1
        stack.append(s[end])
        while distinct > k:
            char = stack.pop(0)
            if char not in stack:
                distinct -= 1
            start += 1
        max_len = end-start+1

    return max_len

print (longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)