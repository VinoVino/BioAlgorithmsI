__author__ = 'jcovino'
from sys import argv
"""
CODE CHALLENGE: Find the length of a longest path in the Manhattan Tourist Problem.
     Input: Integers n and m, followed by an n x (m + 1) matrix Down and an (n + 1) x m matrix Right.
     The two matrices are separated by the - symbol.
     Output: The length of a longest path from source (0, 0) to sink (n, m) in the n x m rectangular grid
     whose edges are defined by the matrices Down and Right.

Sample Input:
     4 4
     1 0 2 4 3
     4 6 5 2 1
     4 4 5 2 1
     5 6 8 5 3
     -
     3 2 4 0
     3 2 4 2
     0 7 3 3
     3 3 0 2
     1 3 2 2

Sample Output:
     34

"""


def manhattanTourist(n,m,down,right,Scores):

    print n
    print m
    print down
    print right

    for i in range (n): # down
        Scores[i+1][0]=Scores[i][0] + down[0][i]
    for j in range (m): # right
        Scores[0][j+1]=Scores[0][j] + right[0][j]

    print Scores

    del down[0]
    print list(down)










def main(argv):
    with open(argv[1],"r") as fstream:        # collect data from file -------
        n = int(fstream.readline().rstrip())
        m = int(fstream.readline().rstrip())
        rows=fstream.readlines()

    Down=[]
    Right=[]
    Right2D=[]
    Down2D=[]

    # create 2-d array with python sucks!
    for i in range (n):
        downrow=rows[i].rstrip()
        downrowsplit=downrow.split(' ')
        for element in downrowsplit:
            Down.append(element)
        Down2D.append(Down)
        Down=[]

    for j in range (n+1,n*2+2):
        rightrow=rows[j].rstrip()
        rightrowsplit=rightrow.split(' ')
        for element in rightrowsplit:
            Right.append(element.rstrip())
        Right2D.append(Right)
        Right=[]

     # collect data from file-----------

    Scores = [[0 for i in range(n+1)] for j in range(m+1)]  # create 2 d array with 0s

    Down2Dint=[]
    Right2Dint=[]
    tempList=[]

    for list in Down2D:   # convert to int
        for element in list:
            temp=int(element)
            tempList.append(temp)
        Down2Dint.append(tempList)
        tempList=[]


    #print Down2Dint
    Down2DintREV=[]
    temp=[]
    for i in range(n+1):     ### reverse orientation of down list so it matches right list
        for element in Down2Dint:
           temp.append(element[i])
        Down2DintREV.append(temp)
        temp=[]


    #print "---", Down2DintREV


    for list in Right2D:   # convert to int
        for element in list:
            temp=int(element)
            tempList.append(temp)
        Right2Dint.append(tempList)
        tempList=[]

    print ""

    #print Down2Dint
    #print Right2Dint
    #print Scores


    manhattanTourist(n,m,Down2DintREV,Right2Dint,Scores)










if __name__== "__main__":
    main(argv)