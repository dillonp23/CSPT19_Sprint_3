

"""
Sprint 3.2 Lecture Notes - Exploring Tree Traversals



"""




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


* UPER - Plan:

    * keywords: max, depth

    - keywords hint at a depth first solution
    - depth = count of nodes from root to furthest leaf
    - use iterative approach with a stack
    - if parent has a child, add to stack and add the depth of the node
    - use a max comparison check to update and keep of the maximum depth for any node as we traverse
"""

from collections import deque

def maxDepth(root):
    if root is None:
        return 0

    stack = deque()
    stack.append((root, 1))
    maxDepth = 1

    while len(stack) > 0:
        curr = stack.pop()
        currNode, currDepth = curr[0], curr[1]

        maxDepth = max(maxDepth, currDepth)

        if currNode.left:
            stack.append((currNode.left, currDepth + 1))

        if currNode.right:
            stack.append((currNode.right, currDepth + 1))

    return maxDepth


"""
Exercise: "230. Kth Smallest Element in a BST" (https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

* Examples:

    Input: root = [3,1,4,null,2], k = 1
    Output: 1


    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3
"""