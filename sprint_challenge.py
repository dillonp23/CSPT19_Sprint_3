

""" Sprint Challenge 3 - Data Structures & Algorithms II """


"""
Exercise 1: You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

* Examples:

    Input:
        root = [10, 5, 15, 3, 7, null, 18]
        lower = 7
        upper = 15
        
    Output:
        32

    
    Input:
        root = [10,5,15,3,7,13,18,1,null,6]
        lower = 6
        upper = 10

    Output:
        23


* UPER - Plan:
    * keywords: BST, inclusive, sum, all values

    - use properties of BST's that we know:
        - left < parent < right
        - we can eliminate values by comparing if a node is in the given range or not
    - use a pre-order DFS
    - if curr_node is greater than upper bound of range, traverse to left
    - if curr_node is less than lower bound of range traverse to right
    - if curr_node in range, begin summing up nodes until outside of range
"""
def csBSTRangeSum(root, lower, upper):
    sum = 0
    
    if root != None:
        if lower <= root.value and root.value <= upper:
            sum += root.value
            
        if lower <= root.value:
            sum += csBSTRangeSum(root.left, lower, upper)
            
        if root.value <= upper:
            sum += csBSTRangeSum(root.right, lower, upper)
        
    return sum




"""
Exercise 2: Given a binary tree, write a function that inverts the tree.

Example:

    Input:
         6
       /   \
      4     8
     / \   / \
    2   5 7   9

    Output:
         6
       /   \
      8     4
     / \   / \
    9   7 5   2
"""
from collections import deque

def csBinaryTreeInvert(root):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        popped = queue.popleft()
        temp = popped.left

        popped.left = popped.right
        popped.right = temp

        if popped.left:
            queue.append(popped.left)
        
        if popped.right:
            queue.append(popped.right)

    return root




"""
Exercise 3: You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1.

graph[a] is a list of all nodes b for which the edge a -> b exists.

* Example:
    Input: graph = [[1, 2],[3],[3],[4],[]]
    Output: [[0,1,3,4], [0,2,3,4]]
"""