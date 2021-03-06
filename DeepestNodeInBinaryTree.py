"""
You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.

Here's a starting point:

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
  # Fill this in.

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print deepest(root)
# (d, 3)
"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val

# find the deepest height
def height_node(node):
    if not node:
        return 0
    return 1 + max(height_node(node.left), height_node(node.right))

# so far only returns level of deepest node
def deepest(node):
    # Fill this in.
    temp = node
    # find the deepest height
    height =  height_node(temp)
    value = []

    # find the value that matches the deepest height
    def get_node(node, h, height):
      if node is None:
          return 

      if h == height:
        value.append(node.val)

      get_node(node.left, h+1, height)
      get_node(node.right, h+1, height)

    get_node(node, 1, height)
    return (value.pop(), height)

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)