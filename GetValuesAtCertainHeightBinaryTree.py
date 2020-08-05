"""
Given a binary tree, return all values given a certain height h.

Here's a starting point:

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  # Fill this in.

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print valuesAtHeight(a, 3)
# [4, 5, 7]

"""
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def valuesAtHeight(root, height):
    # Fill this in.
    result = []
    
    # recursive function inside the function
    def nodesHeight(root, k, height):

        # when root is empty, will break out of the function
        if root is None: 
            return 
        
        # once the current height reaches the target height, add into results
        if k == height: 
            result.append(root.value)
        
        # recursive to get left side adn right side of tree
        nodesHeight(root.left, k+1, height) 
        nodesHeight(root.right, k+1, height) 
    
    # start current height as 1
    nodesHeight(root, 1, height)
    return result

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
