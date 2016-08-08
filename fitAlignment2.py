__author__ = 'jcovino'
from sys import  argv
from Bio.SubsMat import MatrixInfo as matlist

"""
 CODE CHALLENGE: Solve the Fitting Alignment Problem.
     Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
     Output: A highest-scoring fitting alignment between v and w. Use the simple scoring method in which
     matches count +1 and both the mismatch and indel penalties are 1.

Sample Input:
     GTAGGCTTAAGGTTA
     TAGATA

Sample Output:
     2
     TAGGCTTA
     TAGA--TA
"""
def IterativebackTrack(Tr,X,Y,mCord,nCord):
    m = mCord   # columns, m
    n = nCord  # rows, n


    backtrackSeq1=""
    backtrackSeq2=""

    while m > 0 and n > 0:
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

    return finalseq1,finalseq2

def global_Align(X, Y,indelPenalty):
    m = len(X)
    n = len(Y)
    print ""

    C = [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list  # this is the score list
    Tr= [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list   # this is the traceback list

    for i in range (1, n+1):   # initalize row 0
        Tr[0][i]='R'
        C[0][i]=indelPenalty+ C[0][i-1]

    """for j in range(1,m+1):    # initialize column 0
        Tr[j][0]='D'
        C[j][0]=indelPenalty + C[j-1][0]"""

    #print C

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                matchMis = 1
            else:
                matchMis = -1

            C[i][j] = max(C[i][j-1]+indelPenalty, C[i-1][j]+indelPenalty,C[i-1][j-1]+matchMis)  # take max score from previous columns, or from previous row same column (left, or above) or from match/mismatch
                            #right                  #down                   #diag
            if C[i][j]==C[i-1][j-1]+matchMis:
                Tr[i][j]='DIG'
            elif C[i][j]==C[i][j-1]+indelPenalty:
                Tr[i][j]='R'
            else:
                Tr[i][j]='D'
    print ""

     # Get the position of the highest scoring cell corresponding to the end of the shorter word Y
    maxScore=1
    mCordinates=[]
    for i in range(0,m-n+1):
        for j in range (0,n+1):

            tempScore=C[i][j]
            print i, ":", tempScore
            if tempScore >= maxScore:
                maxScore=tempScore
                mCordinates.append(i)

    print mCordinates

    print m
    print n
    nCord=n
    #print "-->", mCord
    #print "-->", nCord


    for mCord in mCordinates:
        print mCord,nCord
        print "fit alignment score", C[mCord][nCord]
        globalSeq1,globalSeq2=IterativebackTrack(Tr,X,Y,mCord,nCord)
        print""




def main(argv):
    
    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print sequence2

    global_Align(sequence1,sequence2,-1)




if __name__== "__main__":
    main(argv)

