

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

# DFS using a stack
def maxDepth(root):
    pass


# BFS solution using a queue
def maxDepthBFS(root):
    pass


# Using recursion/call stack
def maxDepthRecursive(root):
    pass




"""
Exercise 2: "230. Kth Smallest Element in a BST" (https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

* Examples:

    Input: root = [3,1,4,null,2], k = 1
    Output: 1

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3


* Understand:
    * keywords: BST, smallest, 1-indexed

    - the kth smallest index, i.e. if given k=1, return the smallest element
        - k=2 ==> second smallest element
        - k=3 ==> 3rd smallest element, etc, etc
    - remember this is a BST, so smallest elements to left, larger to right
    - utilize the properties of BST to get optimal solution

* Plan:
    - in-order traversal ==> get elements in ascending order
    - traverse down to left most node before incrementing count
    - store recursive call as a temp variable to recurse back up
    - use a count to track the nodes on way back up
    - when count == k, return curr nodes val 

    * Primary function:
        - prepare for recursive helper function
        - k is 1-indexed
        - so if k == 0 or if root is None
            ==>> return None
        - declare a count instance variable starting at 0
        - return helperFunc(root, k)

    * Helper function (recursive):
        - if root has no left child, then its the smallest element of tree
        - otherwise get smallest element by traversing to left most node
        - increment count back up tree
        - implement recursive call stack in order left->parent->right
        - count won't start incrementing until at smallest possible node

        * Step 1: recursive case 1 (left)
            - check if current node has left child
            - store recursive call for left child in temp var
            - return temp var if != None 

        * Step 2: self.count += 1

        * Step 3: base case (if curr node is kth element)
            - if k == count:
                - return node.val
            
        * Step 4: right (recursive case 2)
            - check if current node has right child
            - store recursive call for right child in temp var
            - return temp var if != None

        * Step 5: If curr node is a leaf return
            - return None
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        if root is None or k == 0:
            return None

        # instance var stores count (eliminates need to pass recursively)
        self.count = 0
        return self.kthHelper(root, k)


    def kthHelper(self, root, k):
        # recursive case 1
        if root.left != None:
            temp = self.kthHelper(root.left, k)
            # stops recursive call at leaf to traverse back up tree 
            if temp != None:
                return temp

        self.count += 1
        if self.count == k:
            return root.val

        # recursive case 2
        if root.right != None:
            temp = self.kthHelper(root.right, k)
            # stops recursive call at leaf to traverse back up tree 
            if temp != None:
                return temp

        # node is leaf, return None to pop up call stack
        return None




