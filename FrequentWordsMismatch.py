__author__ = 'jcovino'
from sys import argv

with open(argv[1],"r") as fstream:
    seqInput=fstream.readline()
    patternLengthInput=fstream.readline()
    misMatchInput=fstream.readline()

patternLength=int(patternLengthInput.rstrip())
seq=seqInput.rstrip()
numberMisMatch=int(misMatchInput.rstrip())

patternPosition=[]

def patternPositionCountMismatch(seq,pattern,numberMisMatch):
    match=(len(pattern)-numberMisMatch)         # of bases to match to count, takes into account mismatches
    index=0
    patternList=list(pattern)
    count=0

    while index < len(seq)-len(pattern)+1:               # outerloop
        curString = seq[index:index+len(pattern)]
        curStringList=list(curString)
        j=0
        matchSum=0
        while j < len(pattern):                             #search for number of matches
            if patternList[j]==curStringList[j]:
                matchSum = matchSum + 1
            j = j+1
        if matchSum >= match:                               #Determine if there is a match with mismatches
            count=count+1
        index=index+1
    return (count)

def frequentWords(seq,patternLength,numberMisMatch):
    stopLength=len(seq)-patternLength
    freqPatterns=[]
    countList=[]
    index=0
    while index < stopLength:   #outer loop
        pattern=seq[index:index + patternLength]  # define kmer
        countList.append(patternPositionCountMismatch(seq,pattern,numberMisMatch))  #count hits of kmer
        index=index+1
    print countList
    maxCount=max(countList)  #determine max number of hits
    print maxCount
    j=0
    while j < index:               #move through countList to determine sequence that matches max
        if countList[j]== maxCount:
            freqPatterns.append(seq[j:j+patternLength])
        j=j+1
    return set(freqPatterns)


print "Pattern found: ", frequentWords(seq,patternLength,numberMisMatch)
