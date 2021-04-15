
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