"""
Given a string, find the length of the longest substring without repeating characters.

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Fill this in.
        longest_length = 0
        for i in range(len(s)-1):
            store_array = [ s[i] ]

            for j in range(i+1, len(s)-1):
                if s[j] in store_array:
                    break
                else:
                    store_array.append(s[j])
            
            if len(store_array) > longest_length:
                longest_length = len(store_array)

        return longest_length

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
print(Solution().lengthOfLongestSubstring('GEEKSFORGEEKS'))
# 7