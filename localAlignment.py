__author__ = 'jcovino'
from sys import  argv
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
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
    print"-"
    print sequence2
    print""
    alignments=[]
    matrix = MatrixInfo.pam250




    for a in pairwise2.align.localds(sequence1, sequence2,matrix,-5,-5):
         print(format_alignment(*a))
         alignments.append(a)

    alignments=alignments[0]
    seq1= alignments[0][alignments[3]:alignments[4]]
    seq2= alignments[1][alignments[3]:alignments[4]]
    currentScore=score_pairwise(seq1, seq2, matrix, -5, -5)
    print currentScore
    print seq1
    print len(seq1)
    print seq2
    print len(seq2)


if __name__== "__main__":
    main(argv)

