

"""
Sprint 3.1 CodeSignal Assignment - BST's & Binary Trees:



* Exercise 1: Balanced Binary Tree

You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node 
differ in height by a maximum of 1.

- Examples:

    1. Given the following tree [5,10,25,None,None,12,3]:
          5
         / \
        10  25
           /  \
          12   3

    * return True 


    2. Given the following tree [5,6,6,7,7,None,None,8,8]:
               5
              / \
             6   6
            / \
           7   7
          / \
         8   8
    
    * return False


* UPER - Plan:
    * keywords: height-balanced, subtrees
    
    - when determining whether a root is balanced, we're interested in its children
    - use a traversal that looks at a nodes children to make a determination about the node
    - i.e. we'll use a recursive post-order traversal (children first)
        - left, right, parent
    
    - if height diff between any 2 siblings is greater than 1, then tree is not balanced
    - helper method will recursively iterate down the list in post-order fashion
        - asserts each subtree of entire tree is balanced
        - each node will return either a 0 or 1
        - two children == 0, no children == 0, one child = 1
        - i.e. no more than height diff of 1 between sibling nodes
"""

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def balancedBinaryTree(root):
    return isBalancedHelper(root) != -1
    

def isBalancedHelper(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1


    left_side = isBalancedHelper(root.left)
    right_side = isBalancedHelper(root.right)

    if left_side == -1 or right_side == -1 or abs(left_side - right_side) > 1:
        return -1


    return max(left_side, right_side) + 1




"""
Exercise 2: Minimum Depth Binary Tree

You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum 
depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf 
node. As a reminder, a leaf node is a node with no children.

* Example:
    Given the binary tree [5,7,22,None,None,17,9],

        5
       / \
      7  22
        /  \
       17   9
    your function should return its minimum depth = 2.
"""