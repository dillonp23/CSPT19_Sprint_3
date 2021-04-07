

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