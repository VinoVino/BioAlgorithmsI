__author__ = 'jcovino'
from sys import argv
import itertools

#####Function
def RVC(seq):    #reverse complmenet function
    revComplement=[]
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for element in seq:
        rev=list(element)     #copies sequence list
        rev.reverse()
        comp=rev[:]        # copies reversed list
        comp = [complement[base] for base in comp]   #complement from dictionary
        revComplement.append(''.join(comp))
    return revComplement

###########
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
############

def peptideEncoding(seq,searchSequence):  #Searches for possible peptide/codon sequences in provided sequence
    finalList=[]
    index=0
    j=0
    while j< len(searchSequence):   #outer loop, # of sequences
        pattern=searchSequence[j]
        while index < len(seq)-len(pattern): #inner loop, search pattern in whole sequence
            curString = seq[index:index+len(pattern)]
            if curString==pattern:
                finalList.append(curString)
            index=index+1
        j=j+1
        index=0

    return finalList

def RNAtoDNA(seq):
    DNA=[]
    i=0
    while i < len(seq): # outerloop, run for each sequence in list
        curSeq = seq[i]
        j=0
        curSeqList=list(curSeq)
        while j < len(curSeqList):
            if curSeqList[j]=='U':
                curSeqList[j]='T'
            j=j+1
        DNA.append(''.join(curSeqList))
        i=i+1
    return DNA


def main(argv):
    codonsDict={}

    with open(argv[2],"r") as fstream:
        seq = fstream.readline()
        seq.rstrip()
        aaSeq=fstream.readline()
        aaSeq.rstrip()
        print seq
        print aaSeq

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


    searchSequence= peptideSubstrings(codonsDict,aaSeq) # possible sequences FWD
    print searchSequence
    print len(searchSequence)
    searchSequenceDNA= RNAtoDNA(searchSequence)   # convert to DNA
    finalF = peptideEncoding(seq,searchSequenceDNA)

    print '\n'.join(finalF)


    revCompSearchSeq=RVC(searchSequenceDNA)  # reverse complements
    print len(revCompSearchSeq)
    finalR = peptideEncoding(seq,revCompSearchSeq)

    print '\n'.join(finalR)

    print len(finalF)
    print len(finalR)
    print len(finalF)+len(finalR)
if __name__== "__main__":
    main(argv)