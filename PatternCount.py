#!/usr/bin/env python

__author__ = 'jcovino'
from sys import argv

         #text-some string
         #Pattern-substring searching for
         #RE search
text=""

#with open(argv[1],"r") as fstream:
   # text=fstream.read()
text=raw_input("Enter in seq: ")
print text
print len(text)

#with open(argv[2],"r") as fstream2:
 #   pattern=fstream2.read()
pattern=raw_input("Enter in pattern: ")

print pattern

print len(pattern)

def patterncount(text,pattern):
    index=0
    count=0
    while index < len(text)-len(pattern):
        curString = text[index:index+len(pattern)]
        if curString==pattern:
           count=count+1
        index=index+1
    return count


print "Pattern found: ", patterncount(text,pattern)








                