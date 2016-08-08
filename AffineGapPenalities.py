__author__ = 'jcovino'
from sys import  argv
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

from Bio.SubsMat import MatrixInfo as matlist

"""
CODE CHALLENGE: Solve the Alignment with Affine Gap Penalties Problem.
     Input: Two amino acid strings v and w (each of length at most 100).
     Output: The maximum alignment score between v and w, followed by an alignment of v and w
     achieving this maximum score. Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and
     a gap extension penalty of 1.


Sample Input:
     PRTEINS
     PRTWPSEIN

Sample Output:
     8
     PRT---EINS
     PRTWPSEIN-
"""

def score_match(pair, matrix):
    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]

def score_pairwise(seq1, seq2, matrix, gap_s, gap_e):
    score = 0
    gap = False
    for i in range(len(seq1)):
        pair = (seq1[i], seq2[i])
        if not gap:
            if '-' in pair:
                gap = True
                score += gap_s
            else:
                score += score_match(pair, matrix)
        else:
            if '-' not in pair:
                gap = False
                score += score_match(pair, matrix)
            else:
                score += gap_e
    return score


def main(argv):
    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print"---"
    print sequence2

    alignments=[]
    matrix = matlist.blosum62

    for a in pairwise2.align.globalds(sequence1, sequence2,matrix,-11,-1):
         print(format_alignment(*a))
         alignments.append(a)


    #print "--->", alignments

    """
    scores=[]
    for align in alignments:
        seq1=align[0]
        seq2=align[1]
        currentScore=score_pairwise(seq1, seq2,matrix, -5, -5)
        scores.append(currentScore)
    print "max", max(scores)
    """



if __name__== "__main__":
    main(argv)

