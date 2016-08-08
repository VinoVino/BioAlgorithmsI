__author__ = 'jcovino'
from sys import  argv
from Bio.SubsMat import MatrixInfo as matlist

"""
Levenshtein introduced edit distance but did not describe an algorithm for computing it, which we leave to you.

Edit Distance Problem: Find the edit distance between two strings.
     Input: Two strings.
     Output: The edit distance between these strings.

CODE CHALLENGE: Solve the Edit Distance Problem.

Sample Input:
     PLEASANTLY
     MEANLY

Sample Output:
     5

https://web.stanford.edu/class/cs124/lec/med.pdf
good explanation
"""


def global_Align(X, Y,indelPenalty):

    """
    -----
   score indels: 1
   score matches: 0
   score mismatches:1
   take min value for each node

    """
    m = len(X)
    #print X, m  # columns, m
    n = len(Y)
    #print Y, n  # rows, n
    print ""

    C = [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list  # this is the score list

    for i in range (1, n+1):   # initalize row 0
        C[0][i]=indelPenalty+ C[0][i-1]

    for j in range(1,m+1):    # initialize column 0
        C[j][0]=indelPenalty + C[j-1][0]


    print C

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                matchMis = 0
            else:
                matchMis = 1

            C[i][j] = min(C[i][j-1]+indelPenalty, C[i-1][j]+indelPenalty,matchMis+C[i-1][j-1])  # take max score from previous columns, or from previous row same column (left, or above) or from match/mismatch
                            #right                  #down                   #diag
    print ""
    #print C


    print "Score ", C[m][n]


def main(argv):
    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print sequence2




    global_Align(sequence1,sequence2,1)    #indel penalty/for edit distance



if __name__== "__main__":
    main(argv)

