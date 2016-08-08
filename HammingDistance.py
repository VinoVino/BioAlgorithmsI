__author__ = 'jcovino'
from sys import argv

#with open(argv[1],"r") as fstream:
 #   input1=fstream.readline()
  #  input2=fstream.readline()

seq1=raw_input("Enter in seq1: ")
seq2=raw_input("Enter in seq2: ")

#seq1=input1.rstrip()
#seq2=input2.rstrip()

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

print hamming(seq1,seq2)