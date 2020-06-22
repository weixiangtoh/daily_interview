"""
You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
Here is the function signature as a starting point (in Python):

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getStrValue(self, node):
        value = ''
        while node:
            value += str(node.val)
            node = node.next
        value = value[::-1]
        return value

    def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        first_value = self.getStrValue(l1)
        second_value = self.getStrValue(l2)
        sum_value_reversed = str(int(first_value) + int(second_value))[::-1]

        # initialise result and temp obejcts --> equate result and temp so that when temp changes, result also change!
        result = ListNode(int(sum_value_reversed[0]))
        temp = result
        sum_value_reversed = sum_value_reversed[1:]
        
        # temp.next that is equal to the ListNode ==> cos the temp is alr filled!, need to fill the next one
        # temp = temp.next --> keep adding .next function into the temp so the can continue for as long as the length of the sum
        while len(sum_value_reversed) > 0:
            char = int(sum_value_reversed[0])
            temp.next = ListNode(char)
            sum_value_reversed = sum_value_reversed[1:]
            temp = temp.next
        
        return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8