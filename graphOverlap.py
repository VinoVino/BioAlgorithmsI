__author__ = 'jcovino'
from sys import argv
from random import randint
"""   Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
ATGCG
GCATG
CATGC
AGGCA
GGCAT
Sample Output:
AGGCA -> GGCAT
CATGC -> ATGCG
GCATG -> CATGC
GGCAT -> GCATG
"""


def suffix(seq):
    suffixSeq=seq[1:]
    #print "suffix ", suffixSeq
    return suffixSeq

def preFix(seq):

    preFixSeq=seq[:len(seq)-1]
    #print "prefFix ", preFixSeq
    return preFixSeq


def graphOverlap(sequences):
    matrix=[]
    matches=[]
    tempList=[]
    finalMatches=[]

    matrix.append(sorted(sequences))
    matrix.append(sorted(sequences))

    print "matrix ", matrix

    for row in matrix:
        for seq in row:
            for col in row:
                if suffix(seq) == preFix(col):
                    tempList.append(seq)
                    tempList.append(col)
                    matches.append(tempList)
                    tempList=[]
    #print "matches ", matches

    for item in matches:
        if not item in finalMatches:
            finalMatches.append(item)
    #print "final matches ", finalMatches

    formatFinalList=[]
    for element in finalMatches:
        formatFinalList.append(" -> ".join(element))

    return formatFinalList


def main(argv):

    sequences=[]
    with open(argv[1],"r") as fstream:
       sequencesInput = fstream.readlines()

    for element in sequencesInput:
        sequences.append(element.rstrip())


    final=graphOverlap(sequences)
    print "------- "

    outFile=open('Answer.txt','w')
    for element in final:
        outFile.write(element)
        outFile.write("\n")
    outFile.close()






if __name__== "__main__":
    main(argv)