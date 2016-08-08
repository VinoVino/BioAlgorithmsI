__author__ = 'jcovino'
from sys import argv

with open(argv[1],"r") as fstream:
    patternInput=fstream.readline()
    seqInput=fstream.readline()
    misMatchInput=fstream.readline()

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

    while index < len(seq)-len(pattern):           #outer loop
        curString = seq[index:index+len(pattern)]
        curStringList=list(curString)
        j=0
        matchSum=0                                  #count number of matches with this variable
        while j < len(pattern):
            if patternList[j]==curStringList[j]:
                matchSum = matchSum + 1
            j = j+1
        if matchSum >= match:
            patternPosition.append(index)           #matches enough times to be considered a match with mismatches
        index=index+1
    return (patternPosition)

printValue= patternPositionCountMismatch(seq,pattern,numberMisMatch)


print (" ".join(str(e) for e in printValue))
outFile=open('patternPositionCountMisMatch.txt','w')
outFile.write(" ".join(str(e) for e in printValue))
outFile.close()
print len(printValue)



