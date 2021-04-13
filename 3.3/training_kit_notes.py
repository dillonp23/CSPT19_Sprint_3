

"""
Sprint 3.3 - Graphs I


Objective 1: Introduction to Graphs

* Graphs
    - collections of related data
    - similar to trees
    - connections can be made from a node to any other node in graph
    - can be in the form of a loop
    - all trees are graphs, but not all graphs are trees


    * Building Blocks
        1. vertices
            - nodes in a graph are called "vertices" or "verts"
        
        2. edges
            - connections in a graph are called "edges"
            - an edge denotes a relationship or linkage between two verts


    * Useful Applications
        - can be used for a wide range of applications
        - easily represent any multi-directional relational data
        
        * examples:
            - cities and their linking roads
            - computers on a network
            - populations of people who know each other and their network ("six degrees")
            - trade relationships between countries
            - money owed in an ongoing poker tournament


    
    * Types of Graphs

        - Directed vs. Undirected Graphs

            a. directed
                - one-way or bidirectional edges
                - at least one edge is not bi-directional
                - data flows from one node to another
                - relationships between verts can be represented with arrows
                - arrow between two nodes can be single direction or bi-directional
                
                - examples:
                    - debt and money owed between different individuals
                    - map of roads within a city
                
        
            b. undirected
                - mutual exchange
                - represent relationships thay aren't necessarily a specific direction

                - examples:
                    - personal connections between users
                        - user A and user B are 'friends', i.e. a mutual relationship
                        - wouldn't make much sense for a directional graph
                    - users who have exchanged goods/services with each other in the past


        - Cyclic vs. Acyclic Graphs

            a. cyclic
                - able to start at a vert, and follow the edges back to starting point

                * important:
                    - any undirected graph is automatically cyclic by definition
                        - you can always travel back along the same edge to starting point
                    
                    - examples:
                        * = side that head of arrow for an edge is pointing to
                            i.e. B->*C, C->*E, E->*D, D->*B

                                *C
                        A -> B <  > E -> F
                                D*

                        ^ cyclic due to arrows between B, C, D, & E pointing opposite directions
                        - can start from any of the 4 verts and get back to starting point

            b. acyclic
                - unable to start at a vert and use edges to return to starting point
                
                * important:
                    - the appearance of a circle in graph can be misleading
                    - graph may appear to have a cycle by its representation even though its acyclic
                        - for example, if two verts within a graph both point to the same next vert
                        - but if it is a directional graph, and both arrows are in same direction,
                            it makes it acyclic

                    - examples:
                        * = side that head of arrow for an edge is pointing to
                            i.e. B->*C, B->*D, D->*E

                                *C
                        A -> B <  > E -> F
                                *D

                        ^ acyclic due to arrows between B, C, D, & E pointing same direction
                        - can't get back to starting vert as entire graph is directional from left->right


        - Weighted Graphs

            a. weighted
                - weighted graphs have values associated with the edges
                - we call these values "edge weights"
                - weights represent different data in different graphs

                - examples:
                    - in a weighted graph representing a map, weights may represent lengths of roads
                        - higher total weight of a route on map = longer distance
                    - weights can help decide which particular path to take when comparing routes
                    - can assign unnaturally large weights to paths we want to avoid
                        - e.g. Google Maps uses this technique to avoid freeways for walking directions
                        - avoid steep roads, or busy vehicle streets when planning bike routes

                * "Djiksra's Algorithm" is a graph search variant that accounts for edge weights

        
        - Directed Acyclic Graphs (DAGs)
            
            a. DAGs
                - directed graph with no cycles
                - can order vertices linearly in a way that every edge directs from earlier to later in sequence
                - useful for a number of different applications

                - examples:
                    - spreadsheet w/vertices representing cells & edges as a cell's formula using another cells value
                    - milestones & activities of largescale projects w/topological ordering to optimize for time
                    - collections of events and their influence on each other like family trees or version histories
                        - e.g. Git uses a DAG to represent commits
                        - a commit can have a child commit, or multiple child commits i.e. a branch
                        - child can come from one parent commit (or two in the case of a merge conflict)
                        - however there is no way to go back and form a loop in the git commit heirarchy


    
    * Drawing Graphs

        1. draw an undirected graph of 8 verts
            - undirected == no arrows
            - mutual exchange w/bi-directional edges

            A----B----C----E
             \   |    |   /
              \  D----F  /
               \ |  / | /
                \G /  H/


        2. draw a directed graph of 7 verts
            - directed == arrows
            - a directed graph has to have at least one edge that is not bidriectional

            A-->B-->C-->E
             \  |   |
              \ D-->F
               \|
                G


        3. draw a cyclic directed graph of 5 verts
            - ensure it has at least one cycle

            A-->B
            |   |
            C<--D<--E

        
        4. draw a directed acyclic graph (DAG) of 8 verts
            - order vertices linearly such that every edge is directed from early to later in sequence
            - will be using a linear sequence: A, B, C, D, E, F, G, H
            - since its difficult to represent a DAG linearly in code, sequence will be on one line,
                and edges will be denoted on the lines above and below sequence.
                    - arrows on top line represent edges going over the top of verts, and bottom line under verts
                    - vertical lines denote which vert an edge starts at
                    - 'A' is the only vert with two edges originating from it


            |-->|----->|-------->
            A   B   C  D   E  F  G  H 
            |------>|----->|->|---->


        5. draw an undirected graph of 4 verts
            - undirected = no arrows & all edges bidirectional exchange

            A----B
            |    |
            |    |
            C----D


        6. draw a directed graph of 5 verts
            - directed = at least a single one-way edge

            A-----B---->D
            \     |
             E--->C



    * Additional Resources Related to Graphs:
        - https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8
        - https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""




"""
Objective 2: Representing Graphs as Adjacency Lists or Matrices


* Representing Graphs in Code
    - need to understand what type of data will be stored, and what operations are necessary

    1. Adjacency List
        - utilizes a Dictionary and a Set
        - outer dict contains each vert as the key, with the edges represented with a set
        - using a set allows O(1) constant access to edges
        - store graph as a list of vertices
        - each vert holds a list of connected vertices


    2. Adjacency Matrix
        - represented by a two-dimensional array (a list of lists)
        - allows for benefit of built-in edge weights
        - 0 denotes no relationship between verts
        - values != 0 represent edge labels or edge weights
        - drawback is we do not have a built in association between vert values and their index


    * Tradeoffs
        - both implmentations have different strengths and weaknesses and different time/space complexities
        - generally speaking adj. lists are the preferred method as they enable many O(1) operations
        - adj. lists make finding a verts neighbors more strightforward than matrices
        - choosing a graph implementation is a case-by-case basis and depends on factors such as:
            - the size/density of graph
            - what you need to optimize for (space vs time)
            - the properties of the data
            - etc..

        * NOTE: either graph implementation could contain more information by including Vertex and Edge classes

 
    * Time & Space Complexity (Lists vs Matrices)

        V = total # of vertices
        E = total # of edges
        e = average # of edges per vertex


        1. Adjacency Lists

            i. space complexity:

                * space (best case): O(V+E)
                    - consider a sparse graph w/100 vertices and only one edge
                    - an adj. list would store all 100 vertices but only need to store a set with one edge
                    - in comparison, a matrix would need to store 100*100 (10,000) connections even though all but one are 0

                * space (worst-case): O(V^2)
                    - such as with very dense graphs
                    - with dense graphs, lists and matrices both have similar space complexities


            ii. time complexity:
                
                * add vertex: O(1)
                    - simple operation for adj. list

                        /* self.vertices["H"] = set() */

                        
                * remove vertex: O(V)
                    - visit each vert and remove all edges pointing to deleted vert
                    - removing elements from dict and sets is O(1) but visiting all verts makes it linear
                    - removing is inefficient in both adj. lists and matrices, but slightly better in lists


                * add edge: O(1)
                    - efficient in both adj. lists and matrices
                    
                        /* self.vertices[v1].add(v2) */


                * remove edge: O(1)
                    - efficient in both adj. lists and matrices

                        /* self.vertices[v1].remove(v2) */


                * find edge: O(1)
                    - efficient in both adj. lists and matrices

                        /* return v2 in self.vertices[v1] */


                * find all edges: O(1)
                    - simply return the value for key that corresponds to vert in dict

                        /* return self.vertex[v] */


        2. Adjacency Matrices

            i. space complexity:

                * space: O(V^2)
                    - consider a dense graph where all verts points to each other vert
                    - dense graphs = high average # of edges per vertex
                    - with very dense graphs, both lists and matrices will have comparable space complexities
                    - in these scenarios a martix *might* be better suited
                        - lists are more space efficient than dictionaries and sets


            ii. time complexity:
                
                * add vertex: O(V)
                    - add new vert to end of each existing row and add a new row
                    - O(V) in average case
                    - lists in Python have O(1) appends, but when the list is full, its an O(n) operation;
                        therefore, in worst case scenario adding a vertex could be O(V^2) for adj. matrices

                    /*  for v in self.edges:
                            self.edges[v].append(0)
                            v.append([0] * len(self.edges + 1)) 
                    */
                

                * remove vertex: O(V^2)
                    - first remove the verts row, then the column for vert in each row
                    - requires moving everything in each list over, so ultimately quadratic time

                
                * add edge: O(1)
                    - efficient in both adj. lists and matrices

                        /* self.edges[v1][v2] = 1 */

                
                * remove edge: O(1)
                    - efficient in both adj. lists and matrices

                    /* self.edges[v1][v2] = 0 */


                * find edge: O(1)
                    - efficient in both adj. lists and matrices

                        /* return self.edges[v1][v2] > 0 */


                * find all edges: O(V)
                    - more complicated in matrices than adj. lists
                    - need to iterate through entire row and poulate a list of results

                        /*  v_edges = []
                            for v2 in self.edges[v]:
                                if self.edges[v][v2] > 0:
                                    v_edges.append(v2)
                            return v_edges 
                        */



    * Time & Space Summary:

                     space     addV    removeV   addEdge	removeEdge	findEdge	getEdges
        1. Matrix:	 O(V^2)	   O(V)    O(V^2)	 O(1)	    O(1)	    O(1)	    O(V)
        2. List:	 O(V+E)	   O(1)    O(V)	     O(1)	    O(1)	    O(1)	    O(1)


        * Note: in most cases an adjacency list will be a better choice for representing graph data, but in
                scenarios where graphs are weighted or very dense, a matrix could be better suited.
"""

# Graph using adjacent list w/weighted edges, i.e. inner dict instead of a set ==> {verts: {edges: weight}}
class GraphList:
    def __init__(self):
        self.vertices = {
            "A": {"B", 1},
            "B": {"C": 3, "D": 2},
            "C": {},
            "D": {},
            "E": {"D": 1}
        }

# Graph implmentation using adjacent matrix ==> ability to store weighted edges comes built in w/ matrices
class GraphMatrix:
    def __init__(self):
        self.edges = [
            [0,1,0,0,0],
            [0,0,3,2,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
        ]




"""
Objective 3: Implementing User Defined Vertex & Graph Classes


We can use multiple dictionaries to implement the Graph abstract data type in Python

    * Two classes needed for this implementation:
        - both classes will have methods needed to perform basic operations on our graph object

        1. Graph
            - use to keep track of vertices in our graph instance
            - enables mapping of vert names to specific vert objects
            - keeps a count of number of verts in our graph instance

            * Instance variables:
                1. vertices
                    - dictionary of Vertex objects

                2. count
                    - number of verts contained in our graph instance


            * Graph class method operations:
                1. add_vertex(self, value)
                    - initializes new Vertex object from value/data, increments self.count, adds to self.vertices

                2. add_edge(self, vert1, vert2, weight = 0)
                    - creates new connection between two vertices and specifies edge weight

                3. get_vertices(self)
                    - retrieves a list of all vertices in our graph
                        - simply return self.vertices.keys()

                4. __contains__(self, vert)
                    - overrides built-in method to properly work with graph instance

                5. __iter__(self)
                    - overrides built-in method to return list of values for each vertex in our graph instance

                

        2. Vertex
            - represents each vertex contained in our graph instance

            * Instance variables:
                1. value/data
                    - value or whatever type of data the vert is storing 

                2. connections
                    - dictionary of other verts

            
            * Vertex class method operations:
                1. add_connection(self, vert, weight = 0)
                    - adds new vert (and weight if exists) to connections dictionary

                2. get_connections(self)
                    - retrieves all currently connected verts from this verts connections dict

                3. get_value(self)
                    - retrieves value/data stored in vert instance from vert.value (or vert.data)

                4. get_weight(self, otherVert)
                    - gets edge weight from this vert instance to another specified vert
"""
class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}
    
    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight = 0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, otherVert):
        return self.connections[otherVert]



class Graph:
    def __init__(self):
        pass



