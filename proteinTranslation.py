__author__ = 'jcovino'
import argparse
from sys import argv


# translate RNA sequence into aminoAcid sequence
def translate(sequence,condonsDict):
    proteinSeq=[]
    i=0
    while i < len(sequence):
        curString=sequence[i:i+3]
        proteinSeq.append(condonsDict[curString])
        i=i+3

    return proteinSeq


def main(argv):

    codonsDict={}
    seq=raw_input("Enter in sequence: ")
    #with open(argv[2],"r") as fstream:
     #   seq = fstream.readline()
      #  seq.rstrip()

    with open(argv[1],"r") as codonMap:
        for line in codonMap:
            line=line.rstrip()
            tokens=line.split(" ")
            codon = tokens[0]
            if len(tokens) < 2:
                aminoAcid = " "
            else:
                aminoAcid = tokens[1]
            codonsDict[codon]=aminoAcid

    print   ''.join(translate(seq,codonsDict))





if __name__== "__main__":
    main(argv)