__author__ = 'jcovino'
from sys import argv

#with open(argv[1],"r") as fstream:
    #seq=fstream.readline()
seq=raw_input("Enter in skew: ")
skewValues=[]
skewValuesPos=[]

def skew(seq):
    length=len(seq)      # size of list
    skewValues.append(0)
    seqList=list(seq)  # make string into list
    i = 0
    while i < length:
        if seqList[i] == 'G':
            skewValues.append(skewValues[-1]+1)
        elif seqList[i] == 'C':
            skewValues.append(skewValues[-1]-1)
        else:
            skewValues.append(skewValues[-1])
        i = i + 1
    return skewValues

skew(seq)

j=0

while j<len(skewValues):
    if skewValues[j] == max(skewValues):
        skewValuesPos.append(j)
    j=j+1


print " ".join(str(e) for e in skewValuesPos)




