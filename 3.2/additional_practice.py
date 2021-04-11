

"""
Exercise 1: "104. Maximum Depth of Binary Tree" (https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

* Examples:

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Input: root = [1,null,2]
    Output: 2

    Input: root = []
    Output: 0

    Input: root = [0]
    Output: 1


* UPER - Understand:

    * keywords: maximum, depth

    - for a given node, its depth is equal to the sum of all parent nodes before it + 1
    - node with max depth will be a leaf, i.e (node.left and node.right) == None
    - interested in a node with no children, therefore one good approach would be a post-order traversal
        - i.e. if a given nodes children aren't the max depth, then neither is itself
        - allows us to eliminate any parent nodes ==> if a node has children, don't compare it with max
    - each time we move down a level, iterate depth + 1
    - children will inherit depth from parent
    

* UPER - Plan:
    - traverse list in pre-order fashion
    - use recursion to pass root and a depth variable
    - whenever we get to a node with no children return its depth
    - at each parent node get a local max by comparing depth of its left and right children
    - local max of a parent node can then be compared to a global max
        - if local max is greater than global max => update global
        - if local max < global, we know any parent node to current node is also less than global max
    - if at a leaf node, return its depth
    - otherwise if at a parent node return its max
"""
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def maxDepth(self, root):
    pass






"""
Exercise 2: "230. Kth Smallest Element in a BST" (https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

* Examples:

    Input: root = [3,1,4,null,2], k = 1
    Output: 1

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3
"""