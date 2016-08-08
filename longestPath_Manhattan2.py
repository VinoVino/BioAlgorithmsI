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

    print "--->d", len(down[0])
    downLen= len(down[0])  # length of line: 1,0,2,4,3 in down list
    #mLen= len(down[0])
    print "--->r,", len(right[0])
    rightLen=len(right[0])  #length of line: 3,2,4,0 in right list
    #nLen=len(right[0])

    print n
    print m

    for i in range (downLen-1): # down
        Scores[i+1][0]=Scores[i][0] + down[i][0]

    for j in range (rightLen): # right
        Scores[0][j+1]=Scores[0][j] + right[0][j]


    j=1
    while j < rightLen+1:
        i=1
        while i < n+1: # 18 :
            downScore=  down[i-1][j]   +    Scores[i-1][j]
            #down score 0,1  1,1  2,1  3,1....0,2   1,2   2,2
            #score      0,1  1,1  2,1  3,1...0,2    1,2  2,2

            rightScore=   right[i][j-1]   +    Scores[i][j-1]
            #right score 1,0  2,0  3,0.... 1,1   2,1    3,1
            #score       1,0  2,0  3,0...  1,1   2,1    3,1

            if downScore>rightScore:
                Scores[i][j]=downScore
            else:
                Scores[i][j]=rightScore
            i=i+1
        j=j+1

    print "-"
    print Scores

    print Scores[n][m]





def main(argv):
    with open(argv[1],"r") as fstream:        # collect data from file -------
        n = int(fstream.readline().rstrip())
        m = int(fstream.readline().rstrip())
        rows=fstream.readlines()

    Down=[]
    Right=[]
    Right2D=[]
    Down2D=[]


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




    Down2Dint=[]
    Right2Dint=[]
    tempList=[]

    for list in Down2D:   # convert to int
        for element in list:
            temp=int(element)
            tempList.append(temp)
        Down2Dint.append(tempList)
        tempList=[]

    for list in Right2D:   # convert to int
        for element in list:
            temp=int(element)
            tempList.append(temp)
        Right2Dint.append(tempList)
        tempList=[]

    print ""

    nLength=len(Down2Dint)
    print nLength
    mLength=len(Right2Dint)
    print mLength
    Scores = [[0 for i in range(m+1)] for j in range(n+1)]  # create 2 d array with 0s


    manhattanTourist(n,m,Down2Dint,Right2Dint,Scores)



if __name__== "__main__":
    main(argv)