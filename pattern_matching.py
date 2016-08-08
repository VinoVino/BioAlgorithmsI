__author__ = 'jcovino'

from sys import argv
pattern=""
seq=""

with open(argv[1],"r") as fstream:
    seq=fstream.read()

pattern=raw_input("Enter in sequence: ")

print len(pattern)
print len(seq)

sequence=[]
revComplement=[]
patternPosition=[]

complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def patternPositionCount(seq,pattern):
    index=0
    while index < len(seq)-len(pattern):
        curString = seq[index:index+len(pattern)]
        if curString==pattern:
           patternPosition.append(index)
        index=index+1
    return patternPosition

patternPositionCount(seq,pattern)
#revComp.RVC(seq)
#patternPositionCount(seq,pattern)


outFile=open('patternPositionCount.txt','w')
outFile.write (" ".join(str(e) for e in patternPosition))
outFile.close()






