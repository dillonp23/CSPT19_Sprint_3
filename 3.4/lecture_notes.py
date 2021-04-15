
"""
Sprint 3.4 - Graphs II Lecture Notes


* Traversal vs Search:
    - traversal = typically covering entire graph
    - search = typically find item, terminate early and return


* DFS vs BFS:
    - BFS = most useful for shortest/min path


* How to solve any graph problem (an UPER-like framework):

    1. translate into graph terminology
        - what are my vertices, edges and weight?

    2. how would you build a graph?
        - do you need to build it or can you use whatever input data is given to you?

    3. How to traverse/search - DFS or BFS?
        - any auxillary data needed?
        - what data do I need to store?


    * Answering these three steps will help guide you to a solution!
"""




"""
Exercise 1: "797. All Paths From Source to Target" (https://leetcode.com/problems/all-paths-from-source-to-target/)

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, 
and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from 
node i to node graph[i][j]).


* Example:
    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

    Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

    Input: graph = [[1],[]]
    Output: [[0,1]]

    Input: graph = [[1,2,3],[2],[3],[]]
    Output: [[0,1,2,3],[0,2,3],[0,3]]

    Input: graph = [[1,3],[2],[3],[]]
    Output: [[0,1,2,3],[0,3]]



* UPER - Graph Specific Questions:
    1. vertices = graph[i], edges = graph[i][j], no weights
    2. we don't need to build this graph ourselves and we can just use the input data as is
    3. DFS or BFS doesn't matter in this case as long as we traverse all possible paths


* UPER - Plan:
    - keep track of path we're currently on
    - once we encounter last node, return the path we took to get there
"""
from collections import deque, defaultdict

def allPathsSourceTarget(graph):
    destination = len(graph) - 1
    graph = buildGraph(graph)
    stack = deque()
    stack.append((0, [0]))
    res = []

    while len(stack) > 0:
        curr = stack.pop()
        currNode, currPath = curr[0], curr[1]

        if currNode == destination:
            res.append(currPath)
        else:
            for neighbor in graph[currNode]:
                newPath = currPath.copy()
                newPath.append(neighbor)
                stack.append((neighbor, newPath))

    return res


# Auxillary function to build a graph (not needed, but covered it in class)
def buildGraph(edges):
    graph = defaultdict(set)
    for (node, neighbors) in enumerate(edges):
        for neighbor in neighbors:
            graph[node].add(neighbor)
    return graph



print("\nExercise 1 - Iterative Depth-First Traversal:")
print(allPathsSourceTarget([])) # expected: []
print(allPathsSourceTarget([[1],[2],[3],[]])) # expected: [[0, 1, 2, 3]]
print(allPathsSourceTarget([[1],[2],[3],[4],[5],[]])) # expected: [[0, 1, 2, 3, 4, 5]]
print(allPathsSourceTarget([[1,3,7],[7],[5],[5],[],[7],[],[]])) # expected: [[0, 1, 7], [0, 3, 5, 7], [0, 7]]
print(allPathsSourceTarget([[1, 2],[3],[3],[]])) # expected: [[0, 1, 3], [0, 2, 3]]
print(allPathsSourceTarget([[1, 2],[3],[3],[4],[5],[6,8],[9],[9],[9],[]]))
# ^ test case 6 ==> expected: [[0, 1, 3, 4, 5, 6, 9], [0, 1, 3, 4, 5, 8, 9], [0, 2, 3, 4, 5, 6, 9], [0, 2, 3, 4, 5, 8, 9]]


def allPathsSourceTargetRecursive(graph):
    res = []
    if len(graph) == 0:
        return res
    
    return allPathsHelper(graph, 0, len(graph)-1, [0], res)


def allPathsHelper(graph, currNode, destNode, currPath, res):
    if currNode == destNode:
        res.append((currPath))
    else:
        for neighbor in graph[currNode]:
            newPath = currPath.copy()
            newPath.append(neighbor)
            allPathsHelper(graph, neighbor, destNode, newPath, res)

    return res



print("\nExercise 1 - Iterative Depth-First Recursive:")
print(allPathsSourceTargetRecursive([])) # expected: []
print(allPathsSourceTargetRecursive([[1],[2],[3],[]])) # expected: [[0, 1, 2, 3]]
print(allPathsSourceTargetRecursive([[1],[2],[3],[4],[5],[]])) # expected: [[0, 1, 2, 3, 4, 5]]
print(allPathsSourceTargetRecursive([[1,3,7],[7],[5],[5],[],[7],[],[]])) # expected: [[0, 1, 7], [0, 3, 5, 7], [0, 7]]
print(allPathsSourceTargetRecursive([[1, 2],[3],[3],[]])) # expected: [[0, 1, 3], [0, 2, 3]]
print(allPathsSourceTargetRecursive([[1, 2],[3],[3],[4],[5],[6,8],[9],[9],[9],[]]))




"""
Exercise 2: "733. Flood Fill" (https://leetcode.com/problems/flood-fill/)

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, 
"flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of 
the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color 
as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

* Example:

    Input: 
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2

    Output: [[2,2,2],[2,2,0],[2,0,1]]

    Explanation: 
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.
"""