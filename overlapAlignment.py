__author__ = 'jcovino'
from sys import  argv
from Bio.SubsMat import MatrixInfo as matlist

"""
CODE CHALLENGE: Solve the Overlap Alignment Problem.
     Input: Two strings v and w, each of length at most 1000.
     Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of
     v and a prefix w' of w achieving this maximum score. Use an alignment score in which matches count
     +1 and both the mismatch and indel penalties are 2.

Sample Input:
     PAWHEAE
     HEAGAWGHEE

Sample Output:
     1
     HEAE
     HEAG
"""
def IterativebackTrack(Tr,X,Y,mCord,nCord):

    m = mCord
    n = nCord

    backtrackSeq1=""
    backtrackSeq2=""

    while n * m !=0:
        if Tr[m][n]=='DIG': # diagonal
            m=m-1
            n=n-1
            backtrackSeq1=backtrackSeq1 + X[m]
            backtrackSeq2=backtrackSeq2 + Y[n]


        elif Tr[m][n]=='D':  # down
            m=m-1
            backtrackSeq1=backtrackSeq1 + X[m]
            backtrackSeq2=backtrackSeq2 + '-'

        else:  # right 'R'
            n=n-1
            backtrackSeq1=backtrackSeq1 + '-'
            backtrackSeq2=backtrackSeq2 + Y[n]

    finalseq1= backtrackSeq1[::-1] # reverse the sequence so its in the correct direction
    finalseq2= backtrackSeq2[::-1]

    print finalseq1
    print finalseq2






def global_Align(X, Y,indelPenalty):

    m = len(X)
    n = len(Y)

    print ""

    C = [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list  # this is the score list
    Tr= [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list   # this is the traceback list

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                matchMis = 1   #match
            else:
                matchMis = -2  #mismatch

            C[i][j] = max(C[i][j-1]+indelPenalty, C[i-1][j]+indelPenalty,C[i-1][j-1]+matchMis)  # take max score from previous columns, or from previous row same column (left, or above) or from match/mismatch
                            #right                  #down                   #diag

            if C[i][j]==C[i-1][j-1]+matchMis:
                Tr[i][j]='DIG'
            elif C[i][j]==C[i][j-1]+indelPenalty:
                Tr[i][j]='R'
            else:
                Tr[i][j]='D'

    print ""

     #Score the maximum value at the bottom or the rightmost frame, C[m][i]
    maxSpot=0
    for i in range(1,n):
        if C[m][i]>maxSpot:
            maxSpot=C[m][i]
            nCord=i

    mCord=m
    print C
    print C[mCord][nCord]  #Starting point for traceback



    IterativebackTrack(Tr,X,Y,mCord,nCord)

def main(argv):
    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print sequence2




    global_Align(sequence1,sequence2,-2)  #indel



if __name__== "__main__":
    main(argv)

