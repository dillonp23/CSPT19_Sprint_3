

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