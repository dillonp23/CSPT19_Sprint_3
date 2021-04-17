
""" Sprint 3.4 - Graphs II CodeSignal Assignment """



"""
Exercise 1: Friend Circles (task 4 of 4)

There are N students in a baking class together. Some of them are friends, while some are not friends. The students' 
friendship can be considered transitive. This means that if Ami is a direct friend of Bill, and Bill is a direct 
friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students who are either direct 
or indirect friends of some level. That is, the friend circle consists of a person, their friends, their 
friends-of-friends, their friends-of-friends-of-friends, and so on.

Given a N*N matrix M representing the friend relationships between students in the class. If M[i][j] = 1, 
then the ith and jth students are direct friends with each other, otherwise not.

You need to write a function that can output the total number of friend circles among all the students.


* Examples:

    Input:[[1,1,0],
           [1,1,0],
           [0,0,1]]
    Output: 2

    * Explanation: The 0th and 1st students are direct friends, so they are in a friend circle. 
    The 2nd student himself is in a friend circle. So return 2.


    Input:[[1,1,0],
           [1,1,1],
           [0,1,1]]
    Output: 1

    * Explanation: The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
    so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.



* UPER - Understand:
    * keywords: "friend circle", transitive, direct/indirect friend, total circles

    - "friend circle" = a person, their friends, their friends' friends, etc...
    - since we're given a matrix, overlap between rows/colums will determine a circle

* UPER - Graph specific questions:
    1. translate into graph terminology
        - rows in matrix define a single student
        - columns of matrix define the relationships they have
        - overlap between a row & column, where the two students have a '1' == "direct friends"
        - an "indirect friend" == two students that don't have an overlapping 1, but instead share a common
             friend in between that links the two students together

     2. how would you build a graph?
        - we can use the input data as-is since it is in the form of an adjacency matrix

     3. How to traverse/search - DFS or BFS?
        - we want to visit as many vertices as possible
        - we'll use a DFS to traverse all paths and determine whether there are paths connecting all N number of students
        - if all students are connected (either directly or in directly) there will only be 1 friend circle
        - otherwise any students with no overlap will count as a separate circle (even if just one individual)

* UPER - Plan:
    - use a DFS search to traverse edges between students
     - if there is a path from student 0 to student N-1, then there is only one friend circle
     - once we have traversed all possible paths (i.e. all students in visited set), this will be counted as 1 circle
     - the number of additional circles will be defined as the count of remaining students (if no overlap between), 
         or the number of other circles that can be made if other students outside first circle do share overlap
"""
def csFriendCircles(M):
    pass




# test cases w/full explanations beneath:
test_1 = [
[1,0,0,1,0],
[0,1,0,1,0],
[0,0,1,0,1],
[1,1,0,1,0],
[0,0,1,0,1]
]
print(csFriendCircles(test_1))

test_2 = [
[1,0,0,0,0],
[0,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,0],
[0,0,0,0,1]
]
print(csFriendCircles(test_2))

test_3 = [
[1,0,0,0,1,0,1],
[0,1,1,0,0,0,0],
[0,1,1,0,0,0,0],
[0,0,0,1,0,0,0],
[1,0,0,0,1,1,0],
[0,0,0,0,1,1,0],
[1,0,0,0,0,0,1] 
]
print(csFriendCircles(test_3))

""" 
Test cases for exercise 1:

* Example 1:
    [
0   [1,0,0,1,0], * friends: [3]
1   [0,1,0,1,0], * friends: [3]
2   [0,0,1,0,1], * friends: [4]
3   [1,1,0,1,0], * friends: [0,1]
4   [0,0,1,0,1]  * friends: [2]
    ]

    * expected == 2 friend circles total (all direct friendships)
        1. (student 0 <--> student 3 <--> student 1)
        2. (student 2 <--> student 4)


* Example 2:
    [[
0   [1,0,0,0,0], * friends: []
1   [0,1,0,0,0], * friends: []
2   [0,0,1,0,0], * friends: []
3   [0,0,0,1,0], * friends: []
4   [0,0,0,0,1] * friends: []
    ]]

    * expected == 5 friend circles total (no friendships)
        - none of the students in this matrix are friends with each other

        * for row[i] (a student) if the only '1' is column[i], then student has no friends in matrix
            - i.e. if student has empty friends array total_circles += 1


* Example 2:
    [[
0   [1,0,0,0,1,0,1], * friends: [4,6] (direct) & [5] (indirect)
1   [0,1,1,0,0,0,0], * friends: [2]
2   [0,1,1,0,0,0,0], * friends: [1]
3   [0,0,0,1,0,0,0], * friends: []
4   [1,0,0,0,1,1,0], * friends: [0,5] (direct) & [6] (indirect)
5   [0,0,0,0,1,1,0], * friends: [4] (direct) & [0,4,6] (indirect)
6   [1,0,0,0,0,0,1] * friends: [0] (direct) & [4,5] (indirect)
    ]]

    * expected == 3 friend circles total (direct & indirect friendships)
        1. (student 0 <--> student 6 <--> student 4 <--> student 5)
        2. (student 1 <--> student 2)
        3. (student 3)
"""