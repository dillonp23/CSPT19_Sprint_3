

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
                - single or bidirectional
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
"""