__author__ = 'jcovino'
from sys import argv
from collections import defaultdict
"""In general, given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges,
    where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled
    by the i-th (k - 1)-mer in Text. The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes
    in PathGraphk(Text).

    De Bruijn Graph from a String Problem: Construct the de Bruijn graph of a string.
         Input: An integer k and a string Text.
        Output: DeBruijnk(Text)."""

def suffix(seq):
    suffixSeq=seq[1:]
    #print "suffix ", suffixSeq
    return suffixSeq

def preFix(seq):
    preFixSeq=seq[:len(seq)-1]
    #print "prefFix ", preFixSeq
    return preFixSeq


def generateKmers(sequence,kmerLength): # generate all kmers in a given sequence
    kmers=[]
    index=0

    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        kmers.append(sequence[index:index+kmerLength])  #kmer defined
        index = index+1
    return kmers

def deBrujin(kmers,nodes):  #important, nodes are generated down below in def main
    tempList=[]
    matchList=defaultdict(list)

    for kmer in kmers:
        matchList[preFix(kmer)].append(suffix(kmer))

    print"----"
    outFile=open('Answer.txt','w')

    for key in sorted( matchList):
        outFile.write( "{} -> {}".format(key, ','.join(matchList[key])))
        outFile.write("\n")
    outFile.close()


def main(argv):

    with open(argv[1],"r") as fstream:
       kmerLength=int(fstream.readline())
       sequence = fstream.readline().rstrip()

    print sequence

    kmers = generateKmers(sequence,kmerLength)
    print "kmers ", kmers

    nodes=[]
    for kmer in kmers:
        nodes.append(preFix(kmer))
    nodes.append(suffix(kmers[-1]))

    print "nodes ", nodes

    deBrujin(kmers,nodes)




if __name__== "__main__":
    main(argv)