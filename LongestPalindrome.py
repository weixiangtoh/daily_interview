"""
A palindrome is a sequence of characters that reads the same backwards and forwards. 
Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar

"""

class Solution: 
    def is_palindrome(self, substring):
        if substring == substring[::-1]:
            return True
        return False

    def longestPalindrome(self, s):
        # Fill this in.
        longest_len = 0
        longest_palindrome = ""
        for i in range(len(s)):
            store_string = ""

            for j in range(i, len(s)):
                store_string += s[j]

                if self.is_palindrome(store_string) and len(store_string) > longest_len:
                    longest_len = len(store_string)
                    longest_palindrome = store_string
        
        return longest_palindrome

# Test program
print(str(Solution().longestPalindrome("tracecars")))
# racecar
print(str(Solution().longestPalindrome("banana")))
# anana
print(str(Solution().longestPalindrome("million")))
# illi