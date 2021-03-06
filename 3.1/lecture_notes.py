

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

        * keywords: max, deepest, longest

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

* Notes:
    - Leetcode expresses binary trees as:

        [root, left, right, left, right, left...]

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
    res = []
    postorderHelper(root, res)
    return res


def postorderHelper(parent, res):
    # base case(s):
    # think: "when do I need to stop recursive calls?"
    if parent is None:
        return

    # recursive cases, post-order so left first:
    # 1. left child
    if parent.left:
        postorderHelper(parent.left, res)

    # 2. right child
    if parent.right:
        postorderHelper(parent.right, res)
    
    # append value of current node, will unwind call stack
    res.append(parent.value)




"""
Exercise 2: "94. Binary Tree Inorder Traversal" (https://leetcode.com/problems/binary-tree-inorder-traversal/)

Given the root of a binary tree, return the inorder traversal of its nodes' values.

* Notes:
    - Leetcode expresses binary trees as:

        [root, left, right, left, right, left...]

* Examples:

    Input: root = [1,null,2,3]
    Output: [1,3,2]

    Input: root = []
    Output: []

    Input: root = [1]
    Output: [1]

    Input: root = [1,2]
    Output: [2,1]

    Input: root = [1,null,2]
    Output: [1,2]   
"""

def inOrderTraversal(root):
    res = []
    inOrderHelper(root, res)
    return res


def inOrderHelper(parent, res):
    # base case
    if parent is None:
        return

    # in order = left->parent->right
    if parent.left:
        inOrderHelper(parent.left, res)
    
    res.append(parent.value)

    if parent.right:
        inOrderHelper(parent.right, res)




"""
Exercise 3: "94. Binary Tree Preorder Traversal" (https://leetcode.com/problems/binary-tree-preorder-traversal/)

Given the root of a binary tree, return the preorder traversal of its nodes' values.

* Notes:
    - Leetcode expresses binary trees as:

        [root, left, right, left, right, left...]

* Examples:

    Input: root = [1,null,2,3]
    Output: [1,2,3]

    Input: root = []
    Output: []

    Input: root = [1]
    Output: [1]

    Input: root = [1,2]
    Output: [1,2]

    Input: root = [1,null,2]
    Output: [1,2]   
"""

def preOrderTraversal(root):
    res = []
    preorderHelper(root, res)
    return res


def preorderHelper(parent, res):
    if parent is None:
        return

    # preorder = parent, left, right
    res.append(parent.value)

    if parent.left:
        preorderHelper(parent.left, res)

    if parent.right:
        preorderHelper(parent.right, res)




"""
* Breadth-First (BFS) Traversals:

    * keywords: level, row, closest, minimum, width, diameter


        1. Level-order:
            - nodes sequenced based on level of tree they're in
            - start with first level (l0) = root
            - iterate down each level of the tree
            - get nodes straight across from left to right
                - get all nodes for level before moving to next level


            a. "level-order" = process all nodes level by level
                - standard is top level -> bottom level
                - left side -> right side


                    -> -> -> -> -> -> -> -> -> ->

                l0:             root
                l1:          lhs    rhs
                l2:       lhs^rhs  lhs^rhs

                    -> -> -> -> -> -> -> -> -> ->


            b. "reverse level-order" traversal may be classified differently
                depending on the problem, could mean either:
                    * bottom level -> top level

                            and/or

                    * right side -> left side


            * Hint: processes levels of tree in a "level-by-level" fashion
                - first element in sequence is the root, last is bottom-right-most element



    * Implementing a BFS with a queue:
        - nodes in the queue will all be same level
        - process all nodes before moving to next level


    
    * Key differences between DFS and BFS implementations:
        - BFS built on queues (FIFO)
        - DFS built on stacks (LIFO)

        - BFS one vertex selected at a time when visited and marked for queue - slower than DFS
        - DFS only requires reference to parent/children and not the entire tree

        - BFS is a vertex based technique
            - useful for finding the shortest path in a graph
            - useful when search near the source
            - not great for games & puzzles

        - DFS is an edge based technique
            - divide and conquer
            - useful when search far from source
            - good solution for games and puzzles
"""




"""
Exercise 4: "102. Binary Tree Level Order Traversal" (https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

* Examples:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Input: root = [1]
    Output: [[1]]

    Input: root = []
    Output: []


* UPER - Plan:
    * keywords: level order traversal, left to right, level-by-level

    - implement using a deque
    - start by adding root level to queue
    - use iterative approach with a while loop
    - pop nodes off queue and append to result array
    - add all nodes for next level to queue
    - repeat
"""

from collections import deque

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    # returning a nested list ~ [[root], [l0,l0], [l1,l1,l1,l1]]
    queue = deque()
    queue.append(root)
    queue_count = 1
    res = []
    levelOrderHelper(queue, queue_count, res)

    return res


def levelOrderHelper(queue, queue_count, res):
    nodes = []
    level = []

    # pop nodes from queue (corresponds to number of nodes in level)
    while queue_count > 0:
        node = queue.pop()
        if node:
            nodes.append(node)
            level.append(node.val)
            queue_count -= 1
        else:
            return
        
    if len(nodes) == 0:
        return

    for node in nodes:
        # left->right each level - append left 1st
        if node.left != None:
            queue.appendleft(node.left)
            queue_count += 1

        if node.right != None:
            queue.appendleft(node.right)
            queue_count += 1

    res.append(level)

    if queue_count > 0:
        levelOrderHelper(queue, queue_count, res)


#   ^^^    For additonal practice:    ^^^
#   - refactor above solution to use a tuple (parent, left, right) to reduce memory usage




"""
* Characteristics & Subtypes of Binary Trees

* Binary Search Trees (BST's)
    - BST are ordered ==>> left.val < current.val < right.val
    - in order to be a BST, left and right subtrees must also be BSTs
    - for a BST root:
        - the left child to root AND all of its descendants, must be < root.val
        - the right child to root AND all of its descendants, must be > root.val
    - if a problem mentions "BST" you should make use of its properties to get optimal solution
        - balanced BST gives O(log n) for search, insert, and delete operations
        - non-balanced BST gives O(n) operations


    * use an "in-order" traversal (left, current, right) w/ BST ==> get entire tree in ascending order
    * use a "reverse in-order" traversal (right, current, left) w/BST  ==> get entire tree in descending order


* "Perfect" Binary tree ==> every level is completely full, and all leaves on same level
    - each node in tree has either 2 children or none
    - perfect trees have subtrees that terminate at same level 
    - every perfect binary tree is balanced, but not all balanced binary trees are prefect!
    - if leaves are not at same level then this tree could still be 'complete'


* "Degenerate" Binary Tree ==>> every node has at most 1 child
    - no nodes in tree have two children
    - essentially equivalent to a linked list 
    - usually why time/space complexity is O(n)


* Other Defining Characteristics:
        - balanced
            - a tree is "balanced" if there is a max height difference of one child at all levels
        - complete
            - a tree is "complete" if all levels are either completely filled with two
                children per parent, or if tree is only missing right children at the last level                
"""




"""
Exercise 5: "98. Validate Binary Search Tree (https://leetcode.com/problems/validate-binary-search-tree/)

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

* A valid BST is defined as follows:
    - left subtree of a node contains only nodes with keys less than the node's key
    - right subtree of a node contains only nodes with keys greater than the node's key
    - both the left and right subtrees must also be binary search trees
 
* Examples:
    Input: root = [2,1,3]
    Output: true

    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4


* UPER - Plan:
    * keywords: BST, valid

    - valid BST in context of this prompt means tree nodes from left->right == least->greatest
    - we can use a "valid range" to assert entire tree follows valid BST pattern
    - start with root
    - use a depth-first traversal
        - can do iteratively using a Stack
        - can also do recursively and utilize call-stack
    - root has initial valid range from -inf to inf ==>> (float("-inf"),float("inf"))
    - first ensure parent is between upper/lower bounds (exclusive)
        - range w/ parentheses "(lower,upper)" = exclusive vs. brackets "[lower,upper]" = inclusive
    - update lower or upper bound according to parents value
        - if left child ==> (float("-inf"),parent)
            - i.e. if moving to the left, child inherits parents lower bound
            - parent becomes upper bound
        - if right child ==> (parent,float("inf"))
            - i.e. if moving to the right, child inherits parents upper bound
            - parent becomes lower bound
    - iterate to next node and check if within bounds
        - if not, temrinate early and return False
    - if we get to end of function then return True
"""

def isValidBST(root):
    pass