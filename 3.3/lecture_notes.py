

"""
Sprint 3.3 - Graphs I Lecture Notes

Topics:
I. Intro to Graphs
II. Properties
III. Representing Graphs
IV. Graph Traversals


I. Intro to Graphs:
    
    * Common use cases
        a. social network representing users and their connections
        b. flight paths between airports
        c. mind maps (relationships between ideas and words)


    * Components of Graphs:
        1. vertex (nodes)

        2. edges (connections)
            - unidirectional
                e.g. path from B->A but no path from A->B
            
            - bidirectional
                e.g. if A is friends with B, then B is friends with A

        3. weights
            - a value tied to an edge that represents different data in different graphs
            - e.g. distance between two airports in a flight path graph


        * note: binary trees are a subset type of a graph (they're a directed acyclic graph)


    * Graph Properties
        - directed/undirected
        - unidirectional/bidirectional/symmetrical
        - cyclic/acyclic
        - dense/sparse
        - weighted


        a. directed
            - path from A to B, does not imply B to A
                - just because there is an edge between two verts, we want to know which direction

        b. undirected
            - paths between two verts are bidirectional and symmetrical
                - path A to B, implies path B to A

        c. cyclic
            - from a starting point, a path can be taken that will lead back to itself

        d. acyclic
            - no single path in graph that would lead back to itself

        e. dense
            - relative
            - contains close to maximum edges possible
            - the max number of edges in a graph is n^2
                - all verts connected in multiple ways
        
        f. sparse
            - relative
            - contains close to the minimu edges possible
                e.g no edges or single connections

        g. weighted
            - any edge in graph can have a value associated with it

        h. unweighted
            - no edge has an associated value with it



    * Implementing graphs with adjacency lists
        - comprised of an outer dictionary of verts as keys
        - inner set containing the edges for the values
        - adjacencyList[i] is a set of all the edges for vertex i

        example: 
        {
            1: {2, 3},
            2: {4},
            3: {4},
            4: {1}
        }

        ^ nodes 1-4 are the keys for dictionary
        ^ edges for each vert contained w/in a set as values


        * Time & Space Complexity
            - Space: O(vertices^2)
            - Add vertex: O(1)
            - Remove vertex: O(vertices)
            - Add edge: O(1)
            - Remove edge: O(1)
            - Find edge: O(1)
            - Get all edges: O(1)
"""
# Graph class using adjacency lists
class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return str(self.graph)

    def addNode(self, value):
        if value not in self.graph:
            self.graph[value] = set()

    def removeNode(self, value):
        if value in self.graph:
            # remove the key for vert from outer dictionary
            self.graph.pop(value)

            # remove vert from any other set
            for otherNode in self.graph:
                if value in self.graph[otherNode]:
                    self.graph[otherNode].remove(value)


    def addEdge(self, fromNode, toNode):
        self.graph[fromNode].add(toNode)

    def removeEdge(self, fromNode, toNode):
        self.graph[fromNode].remove(toNode)

    def edgeExists(self, fromNode, toNode):
        return toNode in self.graph[fromNode]


myGraph = Graph()
myGraph.addNode(1)
myGraph.addNode(2)
myGraph.addNode(3)
myGraph.addNode(4)
print(myGraph)
myGraph.removeNode(2)
print(myGraph)
myGraph.addEdge(1, 3)
myGraph.addEdge(4, 1)
print(myGraph)
myGraph.removeEdge(4, 1)
print(myGraph.edgeExists(1,3))
myGraph.removeNode(4)
print(myGraph)



"""
* Implementing graphs with adjacency matrices
    - useful for weighted edges
    - use a matrix to represent whether or not there exists an edge between two vertices
    - matrix[i][j] is True if there exists an edge from vertex i to vertex j


    * Time & Space Complexity w/ Matrices
        - Space: O(vertices^2)
        - Even in a sparse graph, but good for dense graphs b/c lists are space efficient
        - Add vertex: O(vertices^2)
        - Remove vertex: O(vertices^2)
        - Add edge: O(1)
        - Remove edge: O(1)
        - Find edge: O(1)
        - Get all edges: O(vertices)


    * Adjacency Lists vs Matrices
        - depends on density of graph and what we want to optimize for
        - if optimizing for space, representing dense graphs with matrices may be better



* Graph Traversals
    - Depth-first and Breadth-first
    - traversal = look at entire graph
    - search = stop once we get to the vert we're instrested in


* Depth-First Traversals
    - traverse in a depth-ward motion using stack/recursion
    - traversals can be different each time
    - keep traversing until node doesn't have neighbors (dead-end) or or all neighbors have already been visited
"""