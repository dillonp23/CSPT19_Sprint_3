

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
"""