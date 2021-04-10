

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
    * keywords: height-balanced, subtrees, children-first => post-order
    
    - when determining whether a root is balanced, we're interested in its children
    - use a traversal that puts node * children-first * to make a determination about the node
    - i.e. we'll use a recursive post-order traversal (children first)
        - left, right, parent
    
    - if height diff between any 2 siblings is greater than 1, then tree is not balanced
    - helper method will recursively iterate down the list in post-order fashion
        - asserts each subtree of entire tree is balanced
        - i.e. no more than height diff of 1 between sibling nodes
        - if difference > 1 at any point, return a flag to terminate function
            - use -1 as termination flag, since -1 is not a valid depth
        - otherwise return max depth(left branch, right branch)
"""

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def balancedBinaryTree(root):
    depth = 0
    return isBalanced(root, depth) != -1
    

def isBalanced(root, depth):
    if root is None:
        return depth

    lhs = isBalanced(root.left, depth + 1)
    rhs = isBalanced(root.right, depth + 1)

    if abs(lhs-rhs) > 1 or lhs == -1 or rhs == -1:
        return -1


    return max(lhs, rhs)


    

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


* UPER - Plan:
    * keywords: minimum, depth

    - similar approach to the first exercise
    - use a depth-first approach with post-order (since we care about the children first)
    - depth is equal to number of nodes to leaf including root
    - use recursion and pass root with a depth parameter
    - use a self.min instance variable
    - check left side for children first, if node is a leaf, self.min = min(depth, self.min)
    - if we're on right branch, we can terminate early once current depth is > self.min
        - i.e. we already know absolute min since we've already checked the left branch
"""

# In order to use an instance variable,
# CodeSignal requires solution to be written as:
def minimumDepthBinaryTree(root):
    return Solution().minimumDepth(root)


class Solution:
    def minimumDepth(self, root):
        inf = float("inf")
        self.min = inf

        # updates self.min from inf -> min height of tree
        self.minDepthHelper(root, depth)
        
        # check if given an empty tree (no root)
        if self.min == inf:
            return 0

        return self.min


    def minDepthHelper(self, root, depth):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            self.min = min(self.min, depth)
            return depth

        lhs = self.minDepthHelper(root.left, depth + 1)
        rhs = self.minDepthHelper(root.right, depth + 1)



#  Alternate solution - use local min instead of instance var:
def minimumDepth(root):
    curr_min = float("inf")
    return minDepthHelper(root, 1, curr_min)


def minDepthHelper(root, depth, curr_min):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return depth

    lhs = minDepthHelper(root.left, depth + 1, curr_min)
    rhs = minDepthHelper(root.right, depth + 1, curr_min)

    # if lhs or rhs == 0 ==>> no node that side
    # use max(lhs, rhs) instead of min to get min height
    # min height in this case is the height of side != 0
    if lhs == 0 or rhs == 0:
        min_height = max(lhs, rhs)
    else:
        # if lhs != 0 and rhs != 0, then min(lhs, rhs) will get min height
        min_height = min(lhs, rhs)

    return min(curr_min, min_height)



"""
* Write an alternate solution to exercise 2 using an iterative/breadth-first approach

* UPER - Plan:
    - use a queue to append all nodes level-by-level
    - before appending a node, ensure it has both children
    - if node has both children, append node to queue
    - otherwise first node w/o children (i.e. first leaf) will be min depth
        - return depth of that node
"""
from collections import deque

def iterativeMinDepth(root):
    if root is None:
        return 0

    depth = 1
    
    curr_level = deque()
    curr_level.append(root)
    
    next_level = deque()
    next = False

    while len(curr_level) != 0 or len(next_level) != 0:
        if next == True:
            temp = next_level.pop()
            curr_level.append(temp)
            
            # once empty, process nodes (if any) in curr_level
            if len(next_level) == 0:
                next = False
                
        else:
            temp = curr_level.pop()

            # check if node is a leaf
            if temp.left is None and temp.right is None:
                return depth
            
            if temp.left:
                next_level.append(temp.left)
            if temp.right:
                next_level.append(temp.right)

            # after popping all items for current level
            # update "next" to refill curr_level on next loop
            # increment depth to match height of next level
            if len(curr_level) == 0 and len(next_level) > 0:
                next = True
                depth += 1
                

    return depth