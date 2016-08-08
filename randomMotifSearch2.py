__author__ = 'jcovino'
from sys import argv
from collections import Counter
from numpy import product
from random import randint
import random


def Scores(kmers):  ########Generate scores of a list of sequences

    hammingTotal=0
    tempSeq=[]
    posSeq=[]  # a list storing the concated sequence at nth positions of kmers
    for i in range(len(kmers[0])):
        for kmer in kmers:
            tempSeq.append(kmer[i])
        tempConcate=''.join(tempSeq)
        posSeq.append(tempConcate)
        del tempSeq[:]

    for concateSeq in posSeq:  # for each position , 0,1,2... in list of Kmers
        concateSeqList=list(concateSeq)  #make into list
        currentCounter=Counter(concateSeqList)    # determine most frequent base
        tempCounter= currentCounter.most_common(1)
        topBaseList= tempCounter[0]  # reduce counter to list
        topBase= topBaseList[0]     # output key in list
        topBaseSeq=topBase*len(concateSeq) # create compare Seq of top occuring base only
        hammingTotal= hammingTotal + hamming(concateSeq,topBaseSeq)

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
        tempProb=product(tempScore)
        if tempProb > TopProb:
            TopProb=tempProb
            TopSeq = kmer

    return TopSeq


def randomGreedyMotif(Sequences,kmerLength):
    allKmers=[]
    for strand in Sequences:
        allKmers.append(generateKmers(strand,kmerLength))  #allKmers, list of lists, each list is generated kmers from  sequence1, or 2 or 3 ect...

    motif=[]
    for element in allKmers:
        random.seed()
        randomNumber=randint(0,len(element)-1)
        motif.append(element[randomNumber])  #initial seed of motifs

    bestMotifs=motif  #initialize bestMotif
    theTruth=True
    i=0
    while i < 300:
        Ascores,Cscores,Gscores,Tscores =genProfile(motif)  # generate profile from motifs

        while theTruth==True:
            currentMotif=[]
            for strand in Sequences:
                currentMotif.append(probScore(strand,kmerLength,Ascores,Cscores,Gscores,Tscores)) # generate best kmer from each strand each using profile from motif

            if Scores(motif) <= Scores(currentMotif):
                theTruth=False
            else:
                motif=currentMotif
                Ascores,Cscores,Gscores,Tscores =genProfile(motif)  # generate profile from motifs

            if Scores(motif) < Scores(bestMotifs):  # if scores is better, lower is better
                print "score--", Scores(currentMotif)
                bestMotifs=motif   # reset bestMotif

         # recreate motif- from random
        motif=[]
        for element in allKmers:   # randomize motif again
            random.seed()
            randomNumber=randint(0,len(element)-1)
            motif.append(element[randomNumber]) #update motif List
        theTruth=True
        i=i+1
        

    return bestMotifs


def main(argv):


    with open(argv[1],"r") as fstream:
       kmerLength=int(fstream.readline())
       tint = int(fstream.readline())
       sequencesInput = fstream.read().rstrip() # rest of sequences

    print kmerLength
    #print tint
    sequences = sequencesInput.splitlines()
    print sequences

    finalPrint= randomGreedyMotif(sequences,kmerLength)

    for element in finalPrint:
        print element

   # Inputs dna: a collection of Strings, all of the same length
   # k: the length of the motifs/kmers to find
   # t: the number of Strings in Dna


if __name__== "__main__":
    main(argv)