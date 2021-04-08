

"""
Sprint 3.1 - Binary Trees & Binary Search Trees

* Binary Trees:
    - comprised of nodes, subtrees, children and leaves
    - each parent node can have up to 2 children - left and/or right
    - leaves are nodes with no children


    * Highlights of Binary Trees:
        - top most node = root
        - node with no children = leaf


    * Properties & Defining Characteristics:
        - balanced
            - a tree is "balanced" if there is a max height difference of one child at all levels
        - complete
            - a tree is "complete" if all levels are either completely filled with two
                children per parent, or if tree is only missing right children at the last level
        - perfect
            - a tree is "perfect" if every parent node has two children, and all leaves are at
                the same level
                - if leaves are not at same level then this tree could still be 'complete'
    

    * Binary Tree Subtypes:
        - Binary Search Tree (BST)
            - a tree in which entire tree follows a specific pattern/order:

                left_child < parent < right_child

            * BST example:

                    6       
                   / \      
                 4     9    
                / \   / \   
               2   5 7   11  


    * Visualizing Trees:
        - ability to recognize the structural representation of a binary tree can aid in algos
        - balanced trees are more efficient ~ O(log n)
        - unbalanced trees less efficient ~ O(n)
        - certain tree structures can be useful when planning test cases and edge cases
        - visualizing helps when setting base cases in your solutions


    * Tree Traversals:
        - necessary in any binary tree problem
        - methods of traversal:

            1. Depth-First Search (DFS)
                a. in-order
                b. pre-order
                c. post-order

            2. Breadth-First Search (BFS)
                a. level-order


    * Depth-First (DFS) Traversals:
        - keywords = max, deepest, longest
        - DFS can be helpful if problem requires you to get to leaf node to do something
            - just a general idea, there are exceptions

            1. In-order:
                - one side first
                - nodes in sorted ascending/descending order if a BST
                - start by traversing down entire left or right branch
                - after reaching end of left/right branch -> traverse up
                - for each level:
                    - process parent
                    - then right (or left if reverse in-order)
                    - repeat

                a. "in-order" = process nodes in ascending order
                    * left -> current -> right

                b. "reverse in-order" = process nodes in descending order
                    * right -> current -> left

                * Hint: processes tree in a "side-to-side" fashion
                    - first element is left-most or right-most leaf of tree
                    - last element is opposite most leaf to first


            2. Pre-order:
                - parent or "inside" first
                - parent -> entire left branch -> entire right branch
                - if reverse: right branch before left branch

                a. "pre-order"
                    * current -> left -> right

                b. "reverse pre-order"
                    * current -> right -> left

                * Hint: processes branches in a "down-and-over" fashion
                    - first element is top most node of tree (i.e. root)
                    - last element is either left-most or right-most leaf


            3. Post-order:
                - children or "outside" first
                - entire left branch -> entire right branch -> parent
                - if reverse: right branch before left branch

                a. "post-order"
                    * left -> right -> current

                b. "reverse post-order"
                    * right -> left -> current

                * Hint: processes branches in a "out-and-up" fashion
                    - first element is left-most or right-most leaf of tree
                    - last element is top-most node of tree (i.e. root)


        
    * Determine the in-order, pre-order, and post-order sequence for the following tree:

                 5       
                / \      
              7     9    
             /     / \   
            10    20  11 

        1. in-order = 10,7,5,20,9,11

        2. pre-order = 5,7,10,9,20,11

        3. post-order = 10,7,20,11,9,5
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

    Input: root = [1,2]
    Output: [2,1]

    Input: root = [1,null,2]
    Output: [2,1]


* UPER - Plan:
    keywords: postorder

    - rather than use a pointer to a child's parent node, we will use recursion
    - call stack will keep any object references we need
    - doing post-order, so our recursive cases will be called in proper order
        - i.e. left recursive case first, then right
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Post order traversal = left->right->parent
def postOrderTraversal(root):
    pass

    # return [int]

def postorderHelper(parent, res):
    # base case(s):
    # in this problem, when would we need to stop recursive calls?

    # recursive cases:
    # 1. left child

    # 2. right child

    return res



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