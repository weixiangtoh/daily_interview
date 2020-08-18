"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Here's a starting point:

class Solution:
  def reverseWords(self, str):
    # Fill this in.

print Solution().reverseWords("The cat in the hat")
# ehT tac ni eht tah
"""
class Solution:
    def reverseWords(self, str):
        # Fill this in.
        result = ""
        word = ""

        for char in str:
            if char != " ":
                word += char
            else:
                result += word[::-1] + char
                word = ""
        
        return result + word[::-1]

if __name__ == "__main__":
    print (Solution().reverseWords("The cat in the hat"))
    print (Solution().reverseWords("The cat in the hat") == "ehT tac ni eht tah")
    # ehT tac ni eht tah