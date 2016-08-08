#!/usr/bin/env python

__author__ = 'jcovino'
from sys import argv

         #text-some string
         #Pattern-substring searching for
         #RE search
text=""

with open(argv[1],"r") as fstream:
    text=fstream.read()
print len(text)
patternLength=raw_input("Enter in length of pattern: ")




# Counts number of times pattern sequence appears in text
def patterncount(text,pattern):
    index=0
    count=0
    while index < len(text)-len(pattern):
        curString = text[index:index+len(pattern)]
        if curString==pattern:
           count=count+1
        index=index+1
    return count

# returns the most frequent patterns fround in text given the length of the pattern
# as input
def frequentWords(text,patternLength):
    stopLength=len(text)-patternLength
    freqPatterns=[]
    countList=[]
    index=0
    while index < stopLength:
        pattern=text[index:index + patternLength]
        countList.append(patterncount(text,pattern))
        index=index+1
    print countList
    maxCount=max(countList)
    print maxCount
    j=0
    while j < index:
        if countList[j]== maxCount:
            freqPatterns.append(text[j:j+patternLength])
        j=j+1
    return set(freqPatterns)


print "Pattern found: ", frequentWords(text,int(patternLength))