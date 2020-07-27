"""
You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

Here's your starting point:

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
  # Fill this in.

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print merge([a, b])
# 123456
"""
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    # Fill this in.
    array = []
    for element in lists:
        while element:
            # ensure that item in element is not inside array and is not a None type
            if element.val not in array and not None:
                array.append(str(element.val))
            element = element.next
    array.sort()
    return "".join(array)

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456