

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


# Implement a second solution using level-order
# BFS solution using a queue
def maxDepthBFS(root):
    if root is None:
        return 0

    queue = deque()
    queue.append((root, 1))
    maxDepth = 1

    while len(queue) > 0:
        curr = queue.popleft()
        currNode, currDepth = curr[0], curr[1]

        maxDepth = max(maxDepth, currDepth)

        if currNode.left:
            queue.append((currNode.left, currDepth + 1))

        if currNode.right:
            queue.append((currNode.right, currDepth + 1))

    return maxDepth

# Both of these solutions are O(n) and O(n)


# Implement a 3rd solution using recursion
# In this solution we will use class methods and instance variables to automatically have maxDepth update
class Solution:
    def maxDepthRecursive(root):
        if root is None:
            return 0

        self.maxDepth = 0
        self.maxDepthHelper(root, 1)

        return self.maxDepth


    def maxDepthHelper(self, root, currDepth):
        if not root.left and not root.right:
            # check if we're at a depth greater than currently seen
            self.max = max(currDepth, self.maxDepth)

        if root.left:
            self.maxDepthHelper(root.left, currDepth + 1)
        
        if root.right:
            self.maxDepthHelper(root.right, currDepth + 1)


    # This recursive solution is O(n) time and space complexity
    # O(n) space for the actual call stack of functions
        # essentially O(n) for left then O(n) for right => O(2n) ==>> utlimately O(n)




"""
Exercise: "230. Kth Smallest Element in a BST" (https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

* Examples:

    Input: root = [3,1,4,null,2], k = 1
    Output: 1

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3


* UPER - Plan:

    * keywords: BST, smallest, 1-indexed

    - the kth smallest index, i.e. if given k=1, return the smallest element
        - k=2 ==> second smallest element
        - k=3 ==> 3rd smallest element, etc, etc
    - remember this is a BST, so smallest elements to left, larger to right
    - utilize the properties of BST to get optimal solution

    - start to left of tree
    - use an in-order traversal ==> will give us the elements in ascending order
    - start by going all the way down to left, once we can't anymore, traverse back up tree
    - use a count to track the nodes on way back up, when count == k return that nodes value
"""

class BST:

    def kthSmallest(self, root):
        self.curr = 0
        return self.kthHelper(root, k)

    def kthHelper(self, root, k):
        # 1st recursive case
        if root.left:
            leftSubtree = self.kthHelper(root.left, k)

            if leftSubtree:
                return leftSubtree
        
        self.curr += 1
        
        # base case
        if self.curr == k:
            return root.val

        # 2nd recursive case
        if root.right:
            rightSubtree = self.kthHelper(root.right, k)

            if rightSubtree:
                return rightSubtree
        
        return 0