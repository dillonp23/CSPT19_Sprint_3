

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