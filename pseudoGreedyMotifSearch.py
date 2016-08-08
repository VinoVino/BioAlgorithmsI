__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
from collections import defaultdict
import operator
import itertools
from numpy import product

def Scores(kmers):  ########Generate scores of a list of sequences
    #print kmers
    hammingTotal=0
    tempSeq=[]
    posSeq=[]  # a list storing the concated sequence at nth positions of kmers
    for i in range(len(kmers[0])):
        for kmer in kmers:
            tempSeq.append(kmer[i])
        tempConcate=''.join(tempSeq)
        posSeq.append(tempConcate)
        del tempSeq[:]

    #print "----from Scores ", posSeq
    for concateSeq in posSeq:  # for each position , 0,1,2... in list of Kmers
        concateSeqList=list(concateSeq)  #make into list
        currentCounter=Counter(concateSeqList)    # determine most frequent base
        tempCounter= currentCounter.most_common(1)
        topBaseList= tempCounter[0]  # reduce counter to list
        topBase= topBaseList[0]     # output key in list
        #print "concateSeq-- ",concateSeq
        topBaseSeq=topBase*len(concateSeq) # create compare Seq of top occuring base only
        #print "topbase seq ", topBase*len(concateSeq)
        #print "hamming ", hamming(concateSeq,topBaseSeq)
        hammingTotal= hammingTotal + hamming(concateSeq,topBaseSeq)
        #print "hammtotal-- ",hammingTotal
    return hammingTotal

def genProfile(kmers): # generates probabilities of each base occuring at each position given a list of Kmers. Generates a profile with probs at each position
    Ascores=[]
    Cscores=[]
    Gscores=[]
    Tscores=[]

    for i in range (len(kmers[0])): # for length of kmer list, number of kmers
        Acount=1       # reset counts for A, C, G ,T
        Ccount=1
        Gcount=1
        Tcount=1
        Ascores.append(1)
        Cscores.append(1)
        Gscores.append(1)
        Tscores.append(1)
        for kmer in kmers:
            if kmer[i] == 'A':
                Acount=Acount+1
            elif kmer[i]== 'C':
                Ccount=Ccount+1
            elif kmer[i]=='G':
                Gcount=Gcount+1
            else:
                Tcount=Tcount+1

            sumNucleotides= float(len(kmers)+4.0)
            #print "sumNucs--", sumNucleotides
            #print "kmers---",kmers
            #print len(kmers)

            #print Acount/sumNucleotides
            Ascores[i] = float(Acount/sumNucleotides)
            Cscores[i] = float(Ccount/sumNucleotides)
            Gscores[i] = float(Gcount/sumNucleotides)
            Tscores[i] = float(Tcount/sumNucleotides)

    return Ascores, Cscores, Gscores, Tscores


def hamming(seq1,seq2): #hamming distance between two strings
    seq1List=list(seq1)
    seq2List=list(seq2)
    count=0
    i=0

    while i < len(seq1):
        if seq1List[i]!= seq2List[i]:
            count=count+1
        i=i+1
    return count


def generateKmers(sequence,kmerLength): # generate all kmers in a given sequence
    kmers=[]
    index=0

    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        kmers.append(sequence[index:index+kmerLength])  #kmer defined
        index = index+1
    return kmers

def probScore (sequence,kmerLength,Ascores,Cscores,Gscores,Tscores): # generates the score using the probs of each base at each position
    scoreDict={}                                                    # returns scoreDict, a list of ranked kmers based on score
    TopProb=0
    kmers = generateKmers(sequence,kmerLength)  #list of all kmers generated
    #print sequence
    #print kmers
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
        #productProb= product(tempScore)
        currentKmer = kmer
        tempProb=product(tempScore)
        if tempProb > TopProb:
            TopProb=tempProb
            TopSeq = kmer

        #scoreDict[kmer] = productProb

    #sortedFinalScore = sorted(scoreDict.items(), key=operator.itemgetter(1),reverse=True) # returns the dictionary sorted as a list, in reverse
    #print ""
    #print sortedFinalScore

    #tempSeqList= sortedFinalScore[0]    #first dictionary item as list
    #print "top score--",tempSeqList

    #returnValue= tempSeqList[0]

    #print"----from ProbScore ", returnValue  # return key, sequence-
    return TopSeq



def greedyMotif(baseSeq,Sequences,kmerLength):
    bestMotifs=[]
    bestMotifs.append(baseSeq[0:kmerLength])   #update best mofits as first kmer in all sequences
    for seq in Sequences:                      #update best motifs
        bestMotifs.append(seq[0:kmerLength])

    #print "best motifs" , bestMotifs

    baseSeqKmers=generateKmers(baseSeq,kmerLength)  #generate all kmers for base seq
    motif=[]
    for kmer in baseSeqKmers:        # for each kmer in baseSeq
        motif=[kmer]            #initialize motif List to kmer
        #print ""
        #print "base seq kmer", motif
        for strand in Sequences:   # move through each strand Sequences
            Ascores,Cscores,Gscores,Tscores =genProfile(motif)  # generate profile from motifs
            nextMotif= probScore(strand,kmerLength,Ascores,Cscores,Gscores,Tscores)
            motif.append(nextMotif)

            #print "motif Score --", Scores(motif)
            #print motif
            #print "best motif score--", Scores(bestMotifs)
            #print bestMotifs

        if Scores(motif) < Scores(bestMotifs):
            bestMotifs=motif

    return bestMotifs



def main(argv):


    with open(argv[1],"r") as fstream:
       kmerLength=int(fstream.readline())
       tint = int(fstream.readline())
       baseSequence=fstream.readline().rstrip() # first sequence
       sequencesInput = fstream.read().rstrip() # rest of sequences

    print kmerLength
    #print tint
    print "base ", baseSequence
    sequences = sequencesInput.splitlines()
    print sequences

    final= greedyMotif(baseSequence,sequences,kmerLength)

    for element in final:
        print element

   # Inputs dna: a collection of Strings, all of the same length
   # k: the length of the motifs/kmers to find
   # t: the number of Strings in Dna


if __name__== "__main__":
    main(argv)

