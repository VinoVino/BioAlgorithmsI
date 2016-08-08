__author__ = 'jcovino'
from sys import argv
import itertools
    #Prints total numbers of RNA sequences that can translate to peptide seq (given)
def peptideSubstrings(codonsDict,aminoAcidSeq):  #finds possible codons for single aminoacids in peptide. Stores possible sequences in list
    possibleSeq=[]
    searchSequence=[]
    i=0
    while i < len(aminoAcidSeq):
        for codon,aminoAcid in codonsDict.items():
            possibleSeq.append([])
            if aminoAcid == aminoAcidSeq[i]:
                possibleSeq[i].append(codon)
                #foundSubString.append(codon)
        i=i+1

    possibleSeqFiltered= filter(None,possibleSeq)  # remove empty list elements
    searchSubstring = combinations(possibleSeqFiltered)  # make all possible combinations

    for element in searchSubstring:
        curString = ''.join(element)
        searchSequence.append(curString)
    return searchSequence


def combinations(list):                         # combines all possible sequences
    allCombinations=[]
    for element in itertools.product(*list):
        allCombinations.append(element)
    return allCombinations


def main(argv):
    codonsDict={}

    aaSeq=raw_input("Enter in aaseq: ")
    #with open(argv[2],"r") as fstream:
     #   aaSeq=fstream.readline()
      #  aaSeq.rstrip()

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


    final= peptideSubstrings(codonsDict,aaSeq)
    print final
    print len(final)


if __name__== "__main__":
    main(argv)