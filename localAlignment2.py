__author__ = 'jcovino'
from sys import  argv
from Bio.SubsMat import MatrixInfo as matlist

"""
  CODE CHALLENGE: Solve the Local Alignment Problem.
     Input: Two protein strings written in the single-letter amino acid alphabet.
     Output: The maximum score of a local alignment of the strings, followed by a local alignment of these
     strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty sigma = 5.
  Sample Input:
     MEANLY
     PENALTY

Sample Output:
     15
     EANL-Y
     ENALTY

"""
def IterativebackTrack_local(Tr,X,Y,C,mCord,nCord):
    # set start point
    m = mCord  #start at mCordinate of max value
     # columns, m
    n = nCord # start at nCordinate of max value
     # rows, n

    backtrackSeq1=""
    backtrackSeq2=""
    print C[m][n]

    #while m > 0 and n > 0:
    while Tr[m][n] > 0:  # while score of cell is greater than zero--local alignment rule
        if Tr[m][n]=='DIG': # diagonal
            m=m-1
            n=n-1
            backtrackSeq1=backtrackSeq1 + X[m]
            backtrackSeq2=backtrackSeq2 + Y[n]

        elif Tr[m][n]=='D':  # down/up
            m=m-1
            backtrackSeq1=backtrackSeq1 + X[m]
            backtrackSeq2=backtrackSeq2 + '-'

        else:  # right 'R/left'
            n=n-1
            backtrackSeq1=backtrackSeq1 + '-'
            backtrackSeq2=backtrackSeq2 + Y[n]

    finalseq1= backtrackSeq1[::-1] # reverse the sequence so its in the correct direction
    finalseq2= backtrackSeq2[::-1]
    print finalseq1
    print finalseq2

    print len(finalseq1)
    print len(finalseq2)

def local_Align(X, Y,matrix,indelPenalty):

    m = len(X)  # columns, m
    n = len(Y)  # rows, n
    print ""

    C = [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list  # this is the score list
    Tr= [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list   # this is the traceback list


    for i in range(1, m+1): # columns
        for j in range(1, n+1):  # rows
            if (X[i-1],Y[j-1]) in matrix:
                matchMis = C[i-1][j-1] + matrix[(X[i-1],Y[j-1])]  # score from match or mismatch, use this if keys are correct order in matrix
            else:
                matchMis = C[i-1][j-1] + matrix[(Y[j-1],X[i-1])]   # score from match or mismatch, else reverse order of keys for matrix

            C[i][j] = max(C[i][j-1]+indelPenalty, C[i-1][j]+indelPenalty,matchMis,0)  #take max score from right,down or diagn
                            #right                  #down                   #dig , zero for local alignment

            # fill out traceback array based on max selection. no path if score is zero, Tr value remains zero
            if C[i][j] > 0:
                if C[i][j]==matchMis:
                    Tr[i][j]='DIG'
                elif C[i][j]==C[i][j-1]+indelPenalty:
                    Tr[i][j]='R'
                else:
                    Tr[i][j]='D'
    print ""
    #print C
    #print Tr

    maxScore=0   #find max score and m(column) and n(row) coordinate of score

    for i in range(1, m+1):
        for j in range(1, n+1):
            tempScore=C[i][j]
            if tempScore > maxScore:
                maxScore=tempScore
                mCord=i
                nCord=j

    #print C
    print "Score ", C[mCord][nCord]
    IterativebackTrack_local(Tr,X,Y,C,mCord,nCord)

def main(argv):

    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print sequence2

    matrix = matlist.pam250  #set scoring matrix!

    local_Align(sequence1,sequence2,matrix,-5)  # last argumnet is indel penalty

if __name__== "__main__":
    main(argv)

