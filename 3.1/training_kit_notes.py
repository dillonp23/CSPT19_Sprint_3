
"""
Sprint 3.1 - Binary Search Trees

Objective 1: Properties of Binary and "Perfect" Trees

* There are many different types of tree data structures. While they all share common motifs,
    each type of tree can be charcaterized by their sub-structures and any specializations

* Binary Trees:
    - each node in the tree can only have a maximum of 2 child nodes
    - children referred to as left or right
    - top most level of tree is known as the root
    - bottom most level of tree are the leaves
        - leaves have no children



* "Perfect" Trees:
    - means each level is full and not any missing nodes
    - i.e. a perfect binary tree means every parent has 2 children
        - if any parent node of tree has a single child != perfect

    * Properties of "perfect" trees:

        1. each levels nodes double as we increment down the length of the tree:
            
                level 0 = 1 (2^0)            o          <---- "root"
                level 1 = 2 (2^1)          o ^ o
                level 2 = 4 (2^2)        o^o   o^o
                level 3 = 8 (2^3)     o^o o^o o^o o^o   <---- "leaves"

                    * total number of nodes in tree = 15

        2. quantity of last levels nodes = (quantity of all other nodes in tree) + 1
            - called the "leaves"
            - this is true because the first level has a single node
            - useful for calculating the height (h) of a tree:

                * h = height (number of levels in tree)
                * n = total number of nodes

                    h = log_2(n + 1)

            - number of nodes (n) in full tree ==>> leaves + (leaves - 1)
                    
                    n = leaves + (leaves - 1)   or   (2 * leaves) - 1

            - if height is known, solve for total # of nodes (n) using:

                    n = (2^h) - 1
"""
from math import log2, floor

# basic example of a binary tree node
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# given a perfect tree with 127 total nodes, find the height:
n = 127
height = floor(log2(n + 1))
print(height)


# given a perfect tree, with 256 leaves, find the height:
leaves = 256
n = leaves + (leaves - 1)
height = floor(log2(n + 1))
print(height)

# or

n = (2 * leaves) - 1
height = floor(log2(n + 1))
print(height)


# given a perfect tree with a height of 8, find number of nodes:
height = 8
n = (2**height) - 1
print(n)