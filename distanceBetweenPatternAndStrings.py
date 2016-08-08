__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
from collections import defaultdict
import itertools


def hamming(seq1,seq2):
    seq1List=list(seq1)
    seq2List=list(seq2)
    count=0
    i=0

    while i < len(seq1):
        if seq1List[i]!= seq2List[i]:
            count=count+1
        i=i+1
    return count


def distancePatternString(pattern,sequences):
    distanceDict={}
    kmerLength=len(pattern)

    for seq in sequences: # for each sequence in list
        index=0
        temp=[]
        while index < len(seq)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
            curString = seq[index:index+kmerLength]    #kmer defined
            temp.append(hamming(pattern,curString))  #define and store hamming between kmer and pattern
            index = index+1
        distanceDict[seq]=min(temp) #place min value in dictionary

    print sum(distanceDict.values())

def main(argv):

    sequences=[]

    with open(argv[1],"r") as fstream:
       patternSearchInput=fstream.readline()
       sequencesInput = fstream.read().split(" ")

    for element in sequencesInput:
        sequences.append(element.rstrip())

    pattern= patternSearchInput.rstrip()

    print pattern
    print sequences

    distancePatternString(pattern,sequences)



if __name__== "__main__":
    main(argv)