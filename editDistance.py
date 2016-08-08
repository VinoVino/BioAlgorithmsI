__author__ = 'jcovino'
from sys import  argv
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
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
"""
def levenshtein(s1, s2):  #http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def main(argv):
    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print"---"
    print sequence2

    alignments=[]

                            #match,mismatch,opening gap,extending gap
    for a in pairwise2.align.globalms(sequence1, sequence2,0,-1,-1,-1): #these conditions will give the score of edit distance
         print(format_alignment(*a))


    print levenshtein(sequence1,sequence2)  # other way of solving it



if __name__== "__main__":
    main(argv)

