__author__ = 'jcovino'
from sys import argv
from collections import defaultdict
"""DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
     Input: A collection of k-mers Patterns.
     Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
     Sample Input:
GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG
Sample Output:
AGG -> GGG
CAG -> AGG,AGG
GAG -> AGG
GGA -> GAG
GGG -> GGA,GGG





     """

def suffix(seq):
    suffixSeq=seq[1:]
    #print "suffix ", suffixSeq
    return suffixSeq

def preFix(seq):
    preFixSeq=seq[:len(seq)-1]
    #print "prefFix ", preFixSeq
    return preFixSeq

"""
def deBrujin(kmers):
    matchList=defaultdict(list)

    for kmer in kmers:
        matchList[preFix(kmer)].append(suffix(kmer))

    print"----"

    outFile=open('Answer.txt','w')
    for key in sorted( matchList):
        outFile.write( "{} -> {}".format(key, ','.join(matchList[key])))
        outFile.write("\n")
    outFile.close()"""

def deBrujinKmers(kmers):
    tempList=[]
    matchList=defaultdict(list)

    for kmer in sorted(kmers):
        matchList[preFix(kmer)].append(suffix(kmer))

    print matchList
    outFile=open('Answer.txt','w')
    for key in sorted( matchList):
        #print "{} -> {}".format(key, ','.join(matchList[key]))
        outFile.write( "{} -> {}".format(key, ','.join(matchList[key])))
        outFile.write("\n")
    outFile.close()


def main(argv):

    kmers=[]
    with open(argv[1],"r") as fstream:
       kmersInput=fstream.readlines()

    for kmer in kmersInput:
        kmers.append(kmer.rstrip())


    print deBrujinKmers(kmers)





if __name__== "__main__":
    main(argv)
