__author__ = 'jcovino'
from sys import argv
from collections import defaultdict
"""
Sample Input:
2
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA
Sample Output:
GACCGAGCGCCGGA

CODE CHALLENGE: Implement StringSpelledByGappedPatterns.
  """

def suffix(seq):
    suffixSeq=seq[1:]
    #print "suffix ", suffixSeq
    return suffixSeq

def preFix(seq):
    preFixSeq=seq[:len(seq)-1]
    #print "prefFix ", preFixSeq
    return preFixSeq


def genomePath(sequences):
    finalSeq=str(sequences[0])


    for seq in sequences[1:]:
        concate=str(seq[-1])
        finalSeq=finalSeq + concate

    return finalSeq

def stringSpelledGappedPatterns(leftSeq,rightSeq,dlength,klength):
    leftStrings=''
    rightStrings=''
    combinedString=''

    leftStrings=genomePath(leftSeq)
    rightStrings=genomePath(rightSeq)

    print "left", leftStrings
    print "right", rightStrings


    if rightStrings.startswith(leftStrings[dlength+klength:]):
        combinedString=combinedString + leftStrings[:dlength+klength] + rightStrings

    print combinedString






def main(argv):
    seq=[]
    leftSeq=[]
    rightSeq=[]
    with open(argv[1],"r") as fstream:
       kmerLength=int(fstream.readline())
       dLenght=int(fstream.readline())

       seqInput=fstream.readlines()

    for element in seqInput:
        seq.append(element.rstrip())

    for item in seq:
        leftSeq.append(item[:kmerLength])
        rightSeq.append(item[kmerLength+1:])

    print seq

    print "left", leftSeq
    print "right",rightSeq
    stringSpelledGappedPatterns(leftSeq,rightSeq,dLenght,kmerLength)


if __name__== "__main__":
    main(argv)