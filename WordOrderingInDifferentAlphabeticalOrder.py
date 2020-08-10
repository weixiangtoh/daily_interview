"""
Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.

Example:
Input:
words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

Output: False
Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

Example 2:
Input:
words = ["zyx", "zyxw", "zyxwy"],
order="zyxwvutsrqponmlkjihgfedcba"

Output: True
Explanation: The words are in increasing alphabetical order

Here's a starting point:

def isSorted(words, order):
  # Fill this in.

print isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba")
# False
print isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba")
# True
"""
def isSorted(words, order):
    # Fill this in.

    # get a dictionary of order --> key = character, value = position
    order_dict = {}
    for pos, char in enumerate(list(order)):
        order_dict[char] = pos
    
    # loop thru words and make sure that each char is same or earlier than next item
    for i in range(len(words)-1):
        for j in range(len(words[i])):
            if order_dict[words[i][j]] > order_dict[words[i+1][j]]:
                return False
    
    return True

print (isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print (isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True