__author__ = 'jcovino'
from sys import argv

#with open(argv[1],"r") as fstream:
   # seqInput=fstream.readline()
    #patternInput=fstream.readline()
    #misMatchInput=fstream.readline()
seqInput=raw_input("Enter in seq: ")
patternInput= raw_input("Enter in pattern ")
misMatchInput=raw_input("Enter in mismatch ")

pattern=patternInput.rstrip()
seq=seqInput.rstrip()
numberMisMatch=int(misMatchInput.rstrip())
patternPosition=[]

print pattern
print seq
print numberMisMatch

def patternPositionCountMismatch(seq,pattern,numberMisMatch):
    match=(len(pattern)-numberMisMatch)         # of bases to match to count
    index=0
    patternList=list(pattern)

    while index < len(seq)-len(pattern)+1:
        curString = seq[index:index+len(pattern)]
        curStringList=list(curString)
        j=0
        matchSum=0
        while j < len(pattern):
            if patternList[j]==curStringList[j]:
                matchSum = matchSum + 1
            j = j+1
        if matchSum >= match:
            patternPosition.append(index)   # position of sequences that show a match with mismatches
        index=index+1
    return (patternPosition)

printValue= patternPositionCountMismatch(seq,pattern,numberMisMatch)

print len(printValue)   #lenght of the list counts how many hits the sequence had
