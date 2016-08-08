__author__ = 'jcovino'

from sys import argv
from random import randint
from collections import defaultdict
import copy
import itertools
from collections import Counter

"""
Given a string Text, a (k,d)-mer is a pair of k-mers in Text separated by distance d. We use the notation (Pattern1|Pattern2) to refer to a a (k,d)-mer whose k-mers are Pattern1 and Pattern2. For example, (ATG|GGG) is a (3,4)-mer in TAATGCCATGGGATGTT. The (k,d)-mer composition of Text, denoted PairedCompositionk,d(Text), is the collection of all (k,d)- mers in Text (including repeated (k,d)-mers). For example, here is PairedComposition3,1(TAATGCCATGGGATGTT):

TAA GCC
 AAT CCA
  ATG CAT
   TGC ATG
    GCC TGG
     CCA GGG
      CAT GGA
       ATG GAT
        TGG ATG
         GGG TGT
          GGA GTT
TAATGCCATGGGATGTT
"""
def generateKmers(sequence,kmerLength): # generate all kmers in a given sequence
    kmers=[]
    index=0

    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        kmers.append(sequence[index:index+kmerLength])  #kmer defined
        index = index+1
    return kmers

def generate_kdmer(seq,kmerL,dLength):
    print
    Length=kmerL*2+dLength

    kdmer=[]

    index=0
    while index < len(seq)-Length+1:
        temp1=seq[index:index+kmerL]
        temp2='|'
        temp3=seq[index+kmerL+dLength:index+kmerL+dLength+kmerL]

        kdmer.append(temp1+temp2+temp3)
        index=index+1

    return sorted(kdmer)




def main(argv):
    seq=raw_input("Enter in seq: ")
    kmerL=int(raw_input("Enter in kmer length: "))
    dLength=int(raw_input("Enter in dLength: "))

    final= generate_kdmer(seq,kmerL,dLength)

    for element in final:
        print "(",element,")",

if __name__== "__main__":
    main(argv)

