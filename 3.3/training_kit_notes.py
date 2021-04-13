

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
        - both implmentations have strengths and weaknesses

        V = total # of vertices
        E = total # of edges
        e = average # of edges per vertex
        
        * space complexity
            a. list: O(V+E)
            
            b. matrix: O(V^2)
"""