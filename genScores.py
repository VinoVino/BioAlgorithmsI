__author__ = 'jcovino'
from sys import argv
from collections import Counter


def Scores(kmers):
    hammingTotal=0
    tempSeq=[]
    posSeq=[]  # a list storing the concated sequence at nth positions of kmers
    for i in range(len(kmers[0])):
        for kmer in kmers:
            tempSeq.append(kmer[i])
        tempConcate=''.join(tempSeq)
        posSeq.append(tempConcate)
        del tempSeq[:]

    print posSeq

    for concateSeq in posSeq:  # for each position , 0,1,2... in list of Kmers
        concateSeqList=list(concateSeq)  #make into list
        currentCounter=Counter(concateSeqList)    # determine most frequent base
        tempCounter= currentCounter.most_common(1)
        topBaseList= tempCounter[0]  # reduce counter to list
        topBase= topBaseList[0]     # output key in list
        #print concateSeq
        topBaseSeq=topBase*len(concateSeq) # create compare Seq of top occuring base only
        #print topBase*len(concateSeq)
        #print hamming(concateSeq,topBaseSeq)
        hammingTotal= hammingTotal + hamming(concateSeq,topBaseSeq)

    return hammingTotal


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


def main(argv):

    kmers= ['CGT','AAG','AAG','AAT','AAT']

    print Scores(kmers)



if __name__== "__main__":
    main(argv)
