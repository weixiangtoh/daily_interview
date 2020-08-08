"""
You are given the preorder and inorder traversals of a binary tree in the form of arrays. 
Write a function that reconstructs the tree represented by these traversals.

Example:
Preorder: [a, b, d, e, c, f, g]
Inorder: [d, b, e, a, f, c, g]

The tree that should be constructed from these traversals is:

    a
   / \
  b   c
 / \ / \
d  e f  g

Here's a start:

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result


def reconstruct(preorder, inorder):
  # Fill this in.

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print tree
# abcdefg
"""
from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return result

def reconstruct(preorder, inorder):
    # Fill this in.
    # inorder arr can use binary search to extract the head nodes
    # first char in preorder is the head

    def buildTree(array):
      if not array:
        return

      mid = int(len(array) / 2)
      root = Node(array[mid])

      root.left = buildTree(array[:mid])
      root.right = buildTree(array[mid+1:])
      return root

    return buildTree(inorder)

if __name__ == "__main__":
  tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                    ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
  print (tree)
  # abcdefg
  
  tree2 = reconstruct(['A', 'B', 'D', 'E', 'C', 'F'],
                      ['D', 'B', 'E', 'A', 'F', 'C'] )
  print(tree2)
  # ABCDEF