"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:
Input: A = "aa", B = "aa"
Output: true
Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:
Input: A = "", B = "aa"
Output: false
Here's a starting point:

class Solution:
  def buddyStrings(self, A, B):
    # Fill this in.

print Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
# True
print Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb')
# False
"""

class Solution:
    def buddyStrings(self, A, B):
        # Fill this in.

        # corner case: when lengths are no the same
        if len(A) != len(B):
            return False

        # corner case: if A and B are the same
        if A == B:
            return True
        
        n = len(A)
        right = ['0']*n

        # convert all strings to list and compare
        replaced = list(A)
        compare = list(B)
        # make sure only one pair of characters is swapped
        count = 0
        for k in range(n-1):
            if replaced[k] != compare[k]:
                if replaced[k+1] != compare[k] and replaced[k] != compare[k+1]:
                    return False
                replaced[k], replaced[k+1] = replaced[k+1], replaced[k]

                count += 1
        
        # corner case if last character is different but the rest is the same
        if count > 1 or "".join(replaced) != B:
            return False
        
        return True

print(Solution().buddyStrings('aa', 'aa'))
# True
print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
print(Solution().buddyStrings('aaaaaaab', 'aaaaaaac'))
# False