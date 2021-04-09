

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
Exercise 2: "230. Kth Smallest Element in a BST" (https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

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
    - use an in-order traversal ==> will give us the elements in ascending order
    - start by going all the way down to left, once we can't anymore, traverse back up tree
    - use a count to track the nodes on way back up, when count == k return that nodes value

    * Step 1: get smallest element of tree
    - store a count variable starting at 0
    - while there is a left child, iterate down to left child and repeat
    - starting from root, traverse down to left most node and continue updating
    - if root has no left child, then root will be the smallest element of tree
    - once we get to smallest element (or if smallest is root), increment count += 1

    * Step 2: base case
    - if k == count:
        return node.val
    
    * Step 3: recursive cases
    - use knowledge of BST's left < parent < right
    - write recursive cases using this knowledge

        * 3a: left (recursive case 1)
            - check if current node has left child
            - recursive call with left child

        * 3b: parent
            - first increment count
            - if count == k:
                return parent.value
        
        * 3a: left (recursive case 2)
            - check if current node has right child
            - recursive call with right child

    * Step 4: End of Function
    - if we get here then there's no kth value in tree
    - return None
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        pass


    def kthHelper(self, parent, k):
        pass










