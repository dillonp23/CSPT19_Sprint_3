

"""
Sprint 3.3 - Graphs I CodeSignal Assignment
"""



"""
Quiz (task 3 of 5): Representing a graph with an adjacency list

Given this graph:
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