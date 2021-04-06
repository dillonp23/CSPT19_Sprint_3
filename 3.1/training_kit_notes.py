
"""
Sprint 3.1 - Binary Search Trees


* There are many different types of tree data structures. While they all share common motifs,
    each type of tree can be charcaterized by their sub-structures and any specializations

* Binary Trees:
    - each node in the tree can only have a maximum of 2 child nodes
    - children referred to as left or right
"""

# basic example of a binary tree node
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None