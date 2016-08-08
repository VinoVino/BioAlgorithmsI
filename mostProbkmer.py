__author__ = 'jcovino'
from sys import argv
from operator import mul
from numpy import product
import itertools
from collections import Counter
from collections import defaultdict
import operator
import itertools

def generateKmers(sequence,kmerLength): # generate all kmers in a given sequence
    kmers=[]
    index=0

    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        kmers.append(sequence[index:index+kmerLength])  #kmer defined
        index = index+1
    return kmers


def probScore (sequence,kmerLength,Ascores,Cscores,Gscores,Tscores): # generates the score using the probs of each base at each position
    scoreDict={}                                                    # returns scoreDict

    kmers = generateKmers(sequence,kmerLength)  #list of all kmers generated

    for kmer in kmers: # for each kmer in kmer list
        tempScore=[]
        kmerList=list(kmer)  # convert to list
        for i in range (kmerLength):  # for length of kmer
            if kmerList[i] == 'A':
                tempScore.append(Ascores[i])
            elif kmerList[i] == 'C':
                tempScore.append(Cscores[i])
            elif kmerList[i] == 'G':
                tempScore.append(Gscores[i])
            else:
                tempScore.append(Tscores[i])
        productProb= product(tempScore)
        scoreDict[kmer] = productProb

    sortedFinalScore = sorted(scoreDict.items(), key=operator.itemgetter(1),reverse=True) # returns the dictionary sorted as a list, in reverse
    tempSeqList= sortedFinalScore[0]    #first dictionary item as list

    print"---- ", tempSeqList[0]  # return key, sequence-
    return tempSeqList[0]

def main(argv):

    sequence=raw_input("Enter in sequence: ")

    with open(argv[1],"r") as fstream:
        #sequence = fstream.readline().rstrip()
        kmerLength = int(fstream.readline())
        aListInput = (fstream.readline().rstrip())
        cListInput = (fstream.readline().rstrip())
        gListInput = (fstream.readline().rstrip())
        tListInput = (fstream.readline().rstrip())

    aList=(aListInput.split(' '))
    cList=(cListInput.split(' '))
    gList=(gListInput.split(' '))
    tList=(tListInput.split(' '))

    #results = map(int, results)
    aList = map(float,aList)
    cList = map(float,cList)
    gList = map(float,gList)
    tList = map(float,tList)

    print "A : ", aList
    print "C : ", cList
    print "G : " ,gList
    print "T : " ,tList

    print probScore(sequence,kmerLength,aList,cList,gList,tList)







if __name__== "__main__":
    main(argv)