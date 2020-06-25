"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. 
Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
class Solution:
  def isValid(self, s):
    # Fill this in.

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
"""


class Solution:
    def isValid(self, s):
        # Fill this in.

        # declare a character stack to store char
        stack = []

        # loop through string expression
        for char in s:
            
            # if character is opening, add into stack
            if char in ["[", "{", "("]:
                stack.append(char)

            # if char is not opening, then it is closing
            else:
                # corner case:
                # first character in string is a closing
                if len(stack) == 0:
                    return False

                # now check if closing corresponds to the last character added in
                # since it is in order, last opening --> first closing, first opening --> last closing
                opening_char = stack.pop()
                if opening_char == "(":
                    if char != ")":
                        return False
                
                if opening_char == "{":
                    if char != "}":
                        return False

                if opening_char == "[":
                    if char != "]":
                        return False 

        # after looping through expression, there should not be any characters left in stack if balanced
        if len(stack) != 0:
            return False

        return True

if __name__ == "__main__":
    # Test Program
    expres = [ "()(){(())" , "" , "([{}])()" , "{()}[]" ]

    for s in expres:
        print(Solution().isValid(s))

    # should return False
    # should return True
    # should return True
    # should return True