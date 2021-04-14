

"""
Sprint 3.3 - Graphs I CodeSignal Assignment
"""



"""
Quiz I (task 3 of 5): Representing a graph with an adjacency list

Given the graph in this image:

    https://codesignal.s3.amazonaws.com/uploads/1601408702086/68747470733a2f2f692e696d6775722e636f6d2f634a366c656b4d2e6a7067.jpeg

    Use an adjacency list to represent this graph.


* Answer:

    class Graph:
        def __init__(self):
            self.vertices = {
                "A": {"B": 1},
                "B": {"C": 3, "D": 2, "E": 1},
                "C": {"E": 4},
                "D": {"E": 2},
                "E": {"F": 3},
                "F": {},
                "G": {"D": 1}
            }
"""





"""
Quiz II (task 4 of 5): Graph representation in Python interpreter

You are given a Vertex and Graph class. Choose the Python code (written in an interactive interpreter) that would
correctly create the graph in this image:

    https://codesignal.s3.amazonaws.com/uploads/1601409897247/68747470733a2f2f692e696d6775722e636f6d2f796931503441462e6a7067.jpeg
"""
class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __repr__(self):
        return "vertex: " + str(self.value) + ", connections: " + str(self.connections)

    def addConnection(self, vert, weight=0):
        self.connections[vert] = weight

    def getConnections(self):
        return self.connections.keys()

    def getValue(self):
        return self.value

    def getWeight(self, vert):
        return self.connections[vert]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def __repr__(self):
        return "\n# of vertices: " + str(self.count) + "\n" + "\n".join([str(vert) for vert in self.vertices.values()])

    def addVertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def addEdge(self, vert_1, vert_2, weight=0):
        if vert_1 not in self.vertices:
            self.addVertex(vert_1)
        if vert_2 not in self.vertices:
            self.addVertex(vert_2)
        self.vertices[vert_1].addConnection(vert_2, weight)

    def getVertices(self):
        return self.vertices.keys()



print("\nAnswer to Quiz II:")
new_graph = Graph()
new_graph.addVertex("A")
new_graph.addEdge("A", "B", 1)
new_graph.addEdge("B", "C", 3)
new_graph.addEdge("B", "D", 2)
new_graph.addEdge("E", "D", 1)
print(new_graph)
print("all vertices:", [str(vert) for vert in new_graph.vertices.keys()])





"""
Exercise 1 (task 5 of 5): Find all paths from vertex A to B

You are given a directed acyclic graph (DAG) that contains N nodes. Write a function that can find all of
the possible paths from node 0, to node N - 1.

* Notes:
    - graph[a] is a list of all nodes b for which the edge a -> b exists
    - results must be returned in sorted order
    - can use any built-in sort method on the results array at end of your function before returning

* Example:

    Input: graph = [[1, 2],[3],[3],[4],[]]
    Output: [[0,1,3,4], [0,2,3,4]]

        * visual representation:

                0--->1
                |    |
                v    v
                2--->3
                     |
                     v
                     4


        * visual (linear) representation:

            |-->|------>|-->
            0   1   2   3   4
            |------>|--->


        * adjacency list representation:

            vertices = {
                0: {1, 2},
                1: {3},
                2: {3},
                3: {4},
                4: {}
            }


* UPER - Understand:
    * keywords: DAG, all paths, 0->N-1

    - DAG so all connections == directed, and no cycle in graph
    - input is a list of lists
    - the outer list represents the number of nodes
    - inner list represents the connections that each vertex has to another:

        * vertices = {
            0: input_list[0], 
            1: input_list[1],
            2: input_list[2],
            3: input_list[3],
            4: input_list[4]
            }

    - if 0th node has no connections, then there is no possible path to node N-1
        - i.e if input_list[0] == [] ===>> output = [] (empty list)

* UPER - Plan:
    - check len(graph) and len(graph[0]), if either == 0, terminate early & return empty list
    - if both len > 0 use a recursive helper function and return the result of that func
    
    - recursive func takes in graph, current path, current vertex, and a result array
    - use a for loop to get the connections for the current vertex in graph
        - copy the current path to a new temp path array
        - append the next vertex
        - check if the next vertex is the last vertex in graph
            - if so, append the temp path to result array
        - else:
            - call recurisve func using updated vertex, and new temp path
"""
def findAllPaths(graph):
    if len(graph) == 0 or len(graph[0]) == 0:
        return []

    return findPathsHelper(graph, [0], 0, [])


def findPathsHelper(graph, path, vert, res):
    for neighbor in graph[vert]:
        new_path = path.copy()
        new_path.append(neighbor)

        if neighbor == len(graph) - 1:
            res.append(new_path)
            res.sort()
        else:
            findPathsHelper(graph, new_path, neighbor, res)

    return res



print("\nExercise 1:")
print(findAllPaths([])) # expected: []
print(findAllPaths([[1],[2],[3],[]])) # expected: [[0, 1, 2, 3]]
print(findAllPaths([[1],[2],[3],[4],[5],[]])) # expected: [[0, 1, 2, 3, 4, 5]]
print(findAllPaths([[1,3,7],[7],[5],[5],[],[7],[],[]])) # expected: [[0, 1, 7], [0, 3, 5, 7], [0, 7]]
print(findAllPaths([[1, 2],[3],[3],[]])) # expected: [[0, 1, 3], [0, 2, 3]]
print(findAllPaths([[1, 2],[3],[3],[4],[5],[6, 8],[9],[9],[9],[]])) 
# ^ test case 6 ==> expected: [[0, 1, 3, 4, 5, 6, 9], [0, 1, 3, 4, 5, 8, 9], [0, 2, 3, 4, 5, 6, 9], [0, 2, 3, 4, 5, 8, 9]]