

"""
Sprint 3.1 - Binary Trees & Binary Search Trees

* Binary Trees are comprised of nodes, subtrees, and leaves
    - parent node can have up to 2 child nodes - left or right
    - leaves are nodes with no children
"""


"""
Exercise 1: "145. Binary Tree Postorder Traversal" (https://leetcode.com/problems/binary-tree-postorder-traversal/)

Given the root of a binary tree, return the postorder traversal of its nodes' values.

* Examples:
    Input: root = [1,null,2,3]
    Output: [3,2,1]

    Input: root = []
    Output: []

    Input: root = [1]
    Output: [1]
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Post order traversal = process left first, then right, then parent
def postorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    self.postOrderTraversalHelper(root, res)
    return res
    
    
def postOrderTraversalHelper(self, currNode, res):
    if currNode == None:
        return

    if currNode.left != None:
        self.postOrderTraversalHelper(currNode.left, res)

    if currNode.right != None:
        self.postOrderTraversalHelper(currNode.right, res)

    res.append(currNode.val)




"""
* Breadth-First Search
    - "level order" traversal
    - can implement using a queue
        - everything in queuue will be represented as a single level of tree

    * keywords: level, row, closest, minimum, width, diameter



Exercise 2: "102. Binary Tree Level Order Traversal" (https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

* Examples:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Input: root = [1]
    Output: [[1]]

    Input: root = []
    Output: []
"""




"""
* Variations of Binary Trees

* BST's
    - BST are ordered ==>> left.val < current.val < right.val
    - in order to be a BST, left and right subtrees must also be BST's
    - if a problem mentions "BST" you should make use of its properties to get optimal solution
        - balanced BST gives O(log n) for search, insert, and delete operations
        - non-balanced BST gives O(n) operations


    * use an "in-order" traversal (left, current, right) with BST ==> get entire tree in ascending order
    * use a "reverse in-order" traversal (right, current, left)  ==> get enitre tree in descending order


* "Perfect" Binary tree ==> every level is completely full
    - each node in tree has either 2 children or none
    - every perfect binary tree is balanced, but not all balanced binary trees are prefect!


* "Degenerate" Binary Tree ==>> every node has at most 1 child
    - usually why time/space complexity is O(n)
"""




"""
Exercise 3: "98. Validate Binary Search Tree (https://leetcode.com/problems/validate-binary-search-tree/)

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

* Example 1:
    Input: root = [2,1,3]
    Output: true
"""