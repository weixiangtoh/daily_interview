"""
You are given the root of a binary search tree. 
Return true if it is a valid binary search tree, and false otherwise. 
Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, 
and all values in the right subtree are greater than or equal to the root.

Here's a starting point:

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
  # Fill this in.

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
print is_bst(a)

#    5
#   / \
#  3   7
# / \ /
"""
class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def check(root):
  if root is None:
    return 
  
  if root.right is not None:
    if root.right.key < root.key:
      return False
      
  if root.left is not None:
    if root.left.key > root.key:
      return False

  check(root.right)
  check(root.left)

def is_bst(root):
  # Fill this in.
  result = check(root)
  if result is None:
    return True

  return False

def isValidBST(root):
  stack=[(root,float("-inf"),float("inf"))]
  while stack:    
    root,lower,higher=stack.pop()
    if not root: continue
    if root.key<=lower or root.key>=higher:
            return False
    stack.append(((root.right),root.val,higher))
    stack.append(((root.left),lower,root.key))
  return True


if __name__ == "__main__":
  a = TreeNode(5)
  a.left = TreeNode(3)
  a.right = TreeNode(7)
  a.left.left = TreeNode(1)
  a.left.right = TreeNode(4)
  print(isValidBST(a))

  b = TreeNode(3)
  b.left = TreeNode(2)
  b.right = TreeNode(5)
  b.right.left = TreeNode(1)
  b.right.right = TreeNode(4)
  print(isValidBST(b))