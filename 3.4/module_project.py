
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
        - we want to get all possible friends for each student
        - we'll use a BFS to traverse all each row and determine whether the student has any friends
        - if all students are connected (either directly or in directly) there will only be 1 friend circle
        - on the flipside if any student has 0 connections it will count as a single circle (even if just one individual)

* UPER - Plan:
    - use a BFS to traverse each row corresponding to a single student
    - if there is a '1' in the j column (as long as i != j), then *set* matrix[j] as a friend
    - we can store each circle of friends as a set
    - if martix[i][j] has a friend, we will see if that friend is already in other set, if so add it, otheriwse start new set
    - after all students have been visited, the number of circles will be equal to the number of sets


    - add all students to a queue
    - iterate through each of the students and find their friends (if any)
    - if student has a friend either add to a current set, or start a new one

    - total_students_count = len(matrix) - 1
    - i = 0
    - j = 0
    - friend_count = 0

    while len(queue) > 0:
        1. if matrix[i][j] == 1:  
            if i != j:
                - add j to a set or start new set with set(i,j) as this is a friendship
                friend_count += 1

            ** if i does equal j, just continue
                - means were at the '1' referring to current student themself
        2. else:
            (check if at least one possible friend for current student)
            - if j == total_students_count:
                - if matrix[i][j] == 0 and friend_count == 0:  <--- (student shares no friends)
                    - increment total_circles += 1
                    
                - i += 1 ==> (increment to next student)
                - j = 0 ==> (reset j)
            else:
                - j += 1
"""






""" 
Test cases for exercise 1:

* Example 1:
    [[
0   [1,0,0,1,0], * friends: [3]
1   [0,1,0,1,0], * friends: [3]
2   [0,0,1,0,1], * friends: [4]
3   [1,1,0,1,0], * friends: [0,1]
4   [0,0,1,0,1]  * friends: [2]
    ]]

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