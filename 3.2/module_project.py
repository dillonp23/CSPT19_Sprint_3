
"""
Sprint 3.2 - BST & Binary Tree Traversals CodeSignal Assignment


Quiz: Tree Traversal Categories (tasks 1-6)

* What are the two primary categories for tree traversal?


    1. Depth-First Traversals (DFS)

        * DFS keywords: "max", "deepest", "longest"

        * DFS highlights:
            - typically utilize Stacks
            - push nodes to Stack, process in order added
            - useful when getting maximum depth, and when concerned with distant nodes
            - memory advantageous as we only need to store a reference to a parent nodes
            - useful when you need to search the entire tree

            a. (reverse) in-order
                - left->parent->right & (right->parent->left)
                - traverses related nodes in a "side-to-side" fahsion
                
                * highlights:
                    - in a BST gets nodes in ascending order (or descending order)
                    - first node in seq = left-most node of tree (or right-most)
                    - last node in seq = right-most (or left-most)


            b. (reverse) pre-order
                - parent->left->right & (parent->right->left)
                - traverses related nodes in a "down-and-out" fashion

                * highlights:
                    - infer something about a node by looking first at its parent
                    - first node in seq = root of tree
                    - last node in seq = left-most node of tree (or right-most)
                

            c. (reverse) post-order
                - left->right->parent & (right->left->parent)
                - traverses related nodes in a "over-and-up" fashon

                * highlights:
                    - infer something about a node by looking first at its children
                    - first node in seq = left-most node of tree (or right-most)
                    - last node in seq = root of tree


    2. Breadth-First Traversals (BFS)

        * BFS highlights:
            "level", "row", "closest", "minimum", "width", "diameter"

        * BFS highlights:
            - typically utilize Queues
            - enqueue all nodes for a level, dequeue & process all nodes, move to next level
            - useful when getting minimum depth, and when concerned with neighbors of a node
            - can be more memory expensive as we store a reference to entire 'frontier' of tree
            - useful when depth of tree can vary and only need a small part of tree for solution

            a. (reverse) level-order
                - start with root, move level-by-level to leaves (or leaves to root)
                - left side of tree to right side of tree
"""





"""
Exercise 1: Binary tree in-order traversal (task 7 of 9)

You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

* Example:

    Input: [2,None,3,4]

    2
     \
      3
     /
    4

    Output: [2,4,3]


* UPER - Plan:

    * keywords: in-order => DFS

    - use an iterative approach with a stack object or a recursive approach using the call stack
    - start by getting left-most node of tree
    - if no left subtree, start with root
    - return a list with node values in-order (left->parent->right)
    - after we get to deepest left-most node append value, continue appending in proper order as stack unwinds
"""
def binaryTreeInOrderTraversal(root):
    node_vals = []
    if root is None:
        return node_vals

    return inOrderTraversalHelper(root, node_vals)


def inOrderTraversalHelper(root, node_vals):
    if root.left is None and root.right is None:
        node_vals.append(root.value)
        return node_vals    
        
    if root.left != None:
        inOrderTraversalHelper(root.left, node_vals)
    
    node_vals.append(root.value)
    
    if root.right != None:
        inOrderTraversalHelper(root.right, node_vals)
        
    return node_vals





"""
Exercise 2: Traverse Tree (task 8 of 9)

Given a binary tree of integers t, return its node values in the following format:

    - The first element should be the value of the tree root
    - The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost
    - The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way

* Note:
    Solve this task without using recursion, since this is what you'll be asked to do during an interview.

* Example:

    For tree:

            1
          /   \
         2     4
          \   /
           3 5

    input: t = {
        "value": 1,
        "left": {
            "value": 2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 4,
            "left": {
                "value": 5,
                "left": null,
                "right": null
            },
            "right": null
        }
    }

    output: [1, 2, 4, 3, 5]


* UPER - Plan:
    * keywords: root first, left to right

    - breadth-first traversal -> use a queue and an iterative approach
    - start with empty queue and append root
    - use while loop with breaking condition being an empty queue
    - pop a node, append its value to list, add any children to queue, move to next iteration/item in queue
    - since we're simply returning a list with items ordered in standard breadth-first fashion, we only need a single queue/while loop
    - use a deque to append items to one end and pop from the other
    - return list of nodes values
"""
from collections import deque

def traverseTree(t):
    res = []
    queue = deque()
    queue.appendleft(t)

    while len(queue) > 0:
        curr = queue.pop()
        if curr:
            res.append(curr.value)
            if curr.left != None:
                queue.appendleft(curr.left)
            if curr.right != None:
                queue.appendleft(curr.right)

    return res