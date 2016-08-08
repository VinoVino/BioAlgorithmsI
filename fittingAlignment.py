__author__ = 'jcovino'
from sys import  argv
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
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

def fitting_alignment(v,w):
    #https://github.com/jschendel/Rosalind/blob/master/Textbook_05H.py
    '''Returns the fitting alignment of strings v and w, along with the associated score.'''
    # Initialize the matrices.
    S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Get the position of the highest scoring cell corresponding to the end of the shorter word w.
    j = len(w)
    i = max(enumerate([S[row][j] for row in xrange(len(w), len(v))]),key=lambda x: x[1])[0] + len(w)
    max_score = str(S[i][j])
    print "maxScore", max_score
    print i, j , "i,j"



    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    print "---", v_aligned
    print "---", w_aligned

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to start of the fitting alignment.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut off v at the ending point of the backtrack.
    v_aligned = v_aligned[i:]

    return max_score, v_aligned, w_aligned

def main(argv):
    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print"---"
    print sequence2

    print ""
    print fitting_alignment(sequence1,sequence2)





if __name__== "__main__":
    main(argv)

