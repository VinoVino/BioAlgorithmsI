__author__ = 'jcovino'
from sys import  argv
from sys import setrecursionlimit
from collections import defaultdict
from random import randint

"""
Use OUTPUTLCS (reproduced below) to solve the Longest Common Subsequence Problem.
     Input: Two strings s and t.
     Output: A longest common subsequence of s and t. (Note: more than one solution may exist,
     in which case you may output any one.)

    OUTPUTLCS(backtrack, v, i, j)--recursive
        if i = 0 or j = 0
            return
        if backtracki, j = "down"
            OUTPUTLCS(backtrack, v, i - 1, j)
        else if backtracki, j = "right"
            OUTPUTLCS(backtrack, v, i, j - 1)
        else
            OUTPUTLCS(backtrack, v, i - 1, j - 1)
            output vi

    IterativeOutputLCS(Backtrack, v, w)
    LCS = an empty string
    i = length of string v
    j = length of string w
    while i > 0 and j > 0
        if Backtrack(i, j) = down
            i = i-1
        else if Backtrack(i,j) = right
            j = j-1
        else if Backtrack(i,j) = diagonal
             i = i-1
            j  = j-1
            LCS = concatenate vi with LCS
    return LCS

Sample Input:
     AACCTTGG
     ACACTGTGA

Sample Output:
     AACTGG

X = "AATCC"
Y = "ACACG"
m = len(X)
n = len(Y)
C = LCS(X, Y)
"""

def IterativebackTrack(C,X,Y):
    backtrackSeq=""
    i=len(X)
    j=len(Y)
    while i > 0 and j > 0:
        if X[i-1]==Y[j-1]: # diagonal
            i=i-1
            j=j-1
            backtrackSeq=backtrackSeq + X[i]
        elif C[i][j-1] < C[i-1][j]:  # down
            i=i-1
        else: #C[i][j-1] > C[i-1][j]: # right
             j=j-1

    final= backtrackSeq[::-1] # reverse the sequence so its in the correct direction
    print final
    print len(final)

def backTrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return backTrack(C, X, Y, i-1, j-1) + X[i-1]   # diagonal - return backtrack seq one base at a time X[-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return backTrack(C, X, Y, i, j-1)  # Right
        else:
            return backTrack(C, X, Y, i-1, j)   # down


def LCS(X, Y):
    m = len(X)
    #print "X", X
    #print m
    n = len(Y)
    #print "Y", Y
    #print n
    print ""
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n+1)] for i in range(m+1)]  # zero out the list

    for i in range(1, m+1):
        for j in range(1, n+1):
            #print X[i-1], " ", Y[j-1]
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1  # add one to score up and over(from diagonal)
                #print C[i][j]
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])  #else take max score from previous columns, or from previous row same column (left, or above)
                #print "not equal-", C[i][j]
                #print "i,j", i,j
        #print " --"
    print C
    return C




def backTrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in backTrackAll(C, X, Y, i-1, j-1)])
    else:
        R = set()
        if C[i][j-1] >= C[i-1][j]:
            R.update(backTrackAll(C, X, Y, i, j-1))
        if C[i-1][j] >= C[i][j-1]:
            R.update(backTrackAll(C, X, Y, i-1, j))
        return R


def main(argv):
    print ""
    with open(argv[1], "r") as fstream:
        X=fstream.readline().rstrip()
        Y=fstream.readline().rstrip()

    setrecursionlimit(3000)
    m=len(X)
    n=len(Y)

    print X
    print m
    print ""
    print Y
    print n


    C=LCS(X,Y)

    #print C
    print ""
    recursiveBackTrack= backTrackAll(C, X, Y, m, n)
    print "--recursive"
    print recursiveBackTrack
    #print len(recursiveBackTrack)
    print "---Iterative"
    IterativebackTrack(C,X,Y)


if __name__== "__main__":
    main(argv)

