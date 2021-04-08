
"""
Sprint 3.1 - Binary Search Trees

Objective 1: Properties of Binary and "Perfect" Trees

* There are many different types of tree data structures. While they all share common motifs,
    each type of tree can be charcaterized by their sub-structures and any specializations

* Binary Trees:
    - each node in the tree can only have a maximum of 2 child nodes
    - children referred to as left or right
    - top most level of tree is known as the root
    - bottom most level of tree are the leaves
        - leaves have no children



* "Perfect" Trees:
    - means each level is full and not any missing nodes
    - i.e. a perfect binary tree means every parent has 2 children
        - if any parent node of tree has a single child != perfect

    * Properties of "perfect" trees:

        1. each levels nodes double as we increment down the length of the tree:
            
                level 0 = 1 (2^0)            o          <---- "root"
                level 1 = 2 (2^1)          o ^ o     
                level 2 = 4 (2^2)        o^o   o^o    
                level 3 = 8 (2^3)     o^o o^o o^o o^o   <---- "leaves"

                    * total number of nodes in tree = 15

        2. quantity of last levels nodes = (quantity of all other nodes in tree) + 1
            - called the "leaves"
            - this is true because the first level has a single node
            - useful for calculating the height (h) of a tree:

                * h = height (number of levels in tree)
                * n = total number of nodes

                    h = log_2(n + 1)

            - number of nodes (n) in full tree ==>> leaves + (leaves - 1)
                    
                    n = leaves + (leaves - 1)   or   (2 * leaves) - 1

            - if height is known, solve for total # of nodes (n) using:

                    n = (2^h) - 1
"""
from math import log2, floor

# basic example of a binary tree node
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# given a perfect tree with 127 total nodes, find the height:
n = 127
height = floor(log2(n + 1))
print(height)


# given a perfect tree, with 256 leaves, find the height:
leaves = 256
n = leaves + (leaves - 1)
height = floor(log2(n + 1))
print(height)

# or

n = (2 * leaves) - 1
height = floor(log2(n + 1))
print(height)


# given a perfect tree with a height of 8, find number of nodes:
height = 8
n = (2**height) - 1
print(n)




"""
Objective 2: Time & Space Complexity, Strengths & Weaknesses, and Common Uses of Binary Search Trees

* One common type of a binary tree is a Binary Search Tree (BST)
    - BST's are binary trees that follow specific rules about how the nodes are stored
        - in BST's, all nodes to left are smaller and all nodes to right are larger
    
    * BST is "balanced":
        1. if height of left and right subtrees differ <= 1 
        2. if both of subtrees are balanced as well

        * examples:

              o       
            o ^ o         <<== balanced
          o^o   o^o             - same depth on both branches
        o^o    o' 'o            - left branch: left side of subtree only one level deeper
                                - right branch: same depth each side even though left/right only 1 node each

              o       
            o ^ o         <<== unbalanced
                 `o             - greater than 1 level deeper on right branch
                   `o



    * Time Complexity

        * Lookups: O(log n) or O (n)
            - balanced BST => O(log n)
            - unbalanced BST => O(n) in worst case
                - if entirely unbalanced, virtually all nodes on one side in a linear fashion
                
        * Insert: O(log n) or O (n)
            - balanced BST => O(log n)
            - unbalanced BST => O(n) in worst case

        * Delete: O(log n) or O (n)
            - balanced BST => O(log n)
            - unbalanced BST => O(n) in worst case


    * Space Complexity

        * O(n)
            - each node takes up space in memory


    * Strengths:
        - primary strength of BST is that its sorted by default
            - can pull out data in order using an in-order traversal
        - effecient searches
            - O(log n)
            - same as sorted array
        - faster insertions/deletions than sorted arrays

        * BST vs Dictionaries:
            - In average-case dictionaries have more efficient operations
            - BST's have more efficient operations in worst cases


    * Weaknesses:
        - only efficient operations if they're balanced
            - more unbalanced == worsening operation efficienies
        - don't have exceptional efficieny in any one operation
            - decent efficiency for a number of diff. operations == good general-purpose data structure 



    * Challenege question: Why does an unbalanced BST's performance degrade?

        - answer: the more unbalanced a BST becomes, the more closely the tree resembles a 
                linear data structure. As such the benefits of O(log n) operations are degraded. 
                In a perfectly balanced BST, with each iteration of an operation, the amount of 
                data that needs to be processed can be cut in half. Therefore the rate of growth 
                for time complexity gets smaller with each iteration. Unbalanced BST's lose this 
                benefit, so time complexity is closer to linear in the worst case vs. logarithmic
                in the best case with a balanced BST.
"""




"""
Objective 3: Constructing Binary Search Trees


Highlights of BST Implementation:

    * Two classes:
        1. node (BSTNode)
            a. properties:
                - value
                - left (node)
                - right (node)

            b. operations:
                - insert(value)
                - search(value)


        2. tree (BST)
            a. properties:
                - root (node)

            b. operations:
                - insert(value)
                - search(value)

    
    * Important characteristics of nodes in BST:
        - left.value < parent.value < right.value
"""

"""
Exercise 1: 

Plan out (in pseudocode) what steps are needed to delete a node from a BST.

- deleting a node is essentially updating the node to be the next in-order node
    - the nodes "successor" is first in-order
    - if the successor is the root, then the deleted nodes left child will replace its spot
    - if deleting a leaf, next in-order will be None

3 cases:
    1. node has no children
    2. node has one child (left or right)
    3. node has both children


- if node has both children, we need to find the next in-order node
    - first in-order node will be the right node
    - if right node has no children, it moves to location of deleted node
- if right node has a left child:
    - recursively check if node has a left child, until we get the value that is 
    greater than deleted node, but less than all other nodes descendant of deleted_node.right 
        - i.e. deepest (least value) left child thats a descendant of deleted node's right
- if right node only has a right node child, new node becomes right node
- continue checking until we reach first in order node
- i.e. until we reach a node with only a right child, or a node with no child
- we iterate continually down the left branch of deleted node.right, until we get to node thats replacing it
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)

    # challenge: implement delete method
    def delete(self, value):
        pass



class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

    def search(self, value):
        self.root.search(value)

    # challenge: implement delete method
    def delete(self, value):
        self.root.delete(value)