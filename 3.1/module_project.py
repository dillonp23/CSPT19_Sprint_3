

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
traverse tree using a breadth first approach
at each level in tree, compare if there is a right and left child for nodes
split children into two branches for each node
no children
    return
one child
    if its child also has a child return false
both children
    continue
"""

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def balancedBinaryTree(root):
    return isBalanced(root.left, root.right)

def isBalanced(left, right):
    if not left and not right:
        return True

    if not left:
        if right.left or right.right:
            return False

    if not right:
        if left.left or left.right:
            return False

    if left:
        return isBalanced(left.left, left.right)

    if right:
        return isBalanced(right.left, right.right)





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