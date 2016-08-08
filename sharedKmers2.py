__author__ = 'jcovino'
from sys import argv
from collections import defaultdict
import sys

"""
Shared k-mers Problem: Given two strings, find all their shared k-mers.
     Input: An integer k and two strings.
     Output: All k-mers shared by these strings, in the form of ordered pairs (x, y).

CODE CHALLENGE: Solve the Shared k-mers Problem.

Sample Input:
     3
     AAACTCATC
     TTTCAAATC

Sample Output:
     (0, 4)
     (0, 0)
     (4, 2)
     (6, 6)

  """
def GenerateRVCKmers(sequence,kmerLength):
    RVCkmers={}
    index=0
    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        subseq=sequence[index:index+kmerLength]
        RVCsubseq= RVC(subseq)
        #print subseq,RVCsubseq
        RVCkmers[index]=RVCsubseq
        index = index+1

    return RVCkmers

def RVC(pattern):    #reverse complmenet function, take seq in as string(not list)
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G','N':'N','o':'o','e':'e','n':'n'}
    revComplement=[]
    seqList=list(pattern)
    seqList.reverse()
          # copies reversed list
    comp = [complement[base] for base in seqList]   #complement from dictionary
    revComplement.append(''.join(comp))
    revComplementPrint= ("\n".join(str(e) for e in revComplement))
    return (revComplementPrint)


def generateKmers(sequence,kmerLength): # generate all kmers in a given sequence and place in dictionary, key=index, value=kmer  ###unique values
    kmers={}
    index=0
    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        kmers[index]=(sequence[index:index+kmerLength])  #kmer defined
        index = index+1
    return kmers

def defaultDictKmers(sequence,kmerLength): # generate all kmers and place in default dict, key =kmers, value = index
    DictList=defaultdict(list)

    index=0
    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        keySeq=sequence[index:index+kmerLength]
        DictList[keySeq].append(index)  #kmer defined
        index = index+1
    return DictList


def sharekmers(seq2, seq1Kmers,seq2KmersDictList,seq1RVC):
    foundX=defaultdict(list)
    foundRVC=defaultdict(list)
    # find matching kmers and index for Seq1 an Seq2
    for seq1_key,seq1_value in seq1Kmers.items():
        if seq1_value in seq2KmersDictList:
            foundX[seq1_key].append(seq2KmersDictList[seq1_value])


    # find matching RVCkmers and index for Seq1 and Seq2
    for seq1RVC_key,seq1RVC_value in seq1RVC.items():
        if seq1RVC_value in seq2KmersDictList:
            foundRVC[seq1RVC_key].append(seq2KmersDictList[seq1RVC_value])


    return foundX,foundRVC



def main(argv):
        with open(argv[1],"r") as fstream:
            kmerLength=int(fstream.readline())
            sequence1Input=fstream.readline()
            sequence2Input=fstream.readline()

            sequence1=sequence1Input.rstrip()
            sequence2=sequence2Input.rstrip()

        seq1Kmers=generateKmers(sequence1,kmerLength)
        #print seq1Kmers

        seq2KmersDictList=defaultDictKmers(sequence2,kmerLength)
        #print seq2KmersDictList

        seq1RVC=GenerateRVCKmers(sequence1,kmerLength)
        #print seq1RVC

        Cord,RVC_Cord= sharekmers(sequence2,seq1Kmers,seq2KmersDictList,seq1RVC)



        Cord_List=[]

        #print Cord
        #print finalRVC
        #print len(final.values())

        #need to print out all key:value pairs into list
        for key,value in Cord.items():
            for item in value:
                temp=[]
                temp.append(key)  # this is X
                temp.append(item)  #this is Y
                Cord_List.append(temp)

        for key,value in RVC_Cord.items():
            for item in value:
                temp=[]
                temp.append(key)  # this is X,
                temp.append(item)  #this is Y
                Cord_List.append(temp)


        #print Cord_List

        finalList=[]
        for element in Cord_List:
            for i in range (0, len(element[1])):
                temp=[]
                temp.append(element[1][i])  # flipped X and Y for sorting- this is y
                temp.append(element[0])   # this is X
                finalList.append(temp)

        #print finalList

        #print len(finalprint)
        #print finalprint

        sortfinalprint= sorted(finalList)

        #print sortfinalprint



        for item in sortfinalprint:
            sys.stdout.write('(')
            print item[1],   #flipped
            sys.stdout.write(', ')
            print item[0], #flipped
            sys.stdout.write(')')
            print

        print"-----"
        """
        f=open('Answer.txt','w')
        for item in sortfinalprint:
            f.write('(')
            f.write(str(item[1]))
            f.write(', ')
            f.write(str(item[0]))
            f.write(')')
            f.write("\n")

        f.close()
        """
if __name__== "__main__":
    main(argv)

