__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
from collections import defaultdict




def convolution(Spectrum,M):
    refSpectrum=Spectrum[:]
    finalList=[]
    for spec  in Spectrum:
        for ref in refSpectrum:
            temp=spec-ref
            print spec, "- ", ref
            if temp > 0:
                finalList.append(temp)
    print finalList
    Mlist= Counter(finalList)
    Mlistkeys=sorted(Mlist.keys())
    print Mlist
    print Mlistkeys

    returnList=[]

    i=0
    while i<= M:
        returnList.append(Mlistkeys[i])
        i=i+1

    print "returnList ", returnList
    #return returnList

def main(argv):
    massDict={}

    input=raw_input("Enter spectrum: ")
    Spectrum = map(int, input.split())
    #with open(argv[2],"r") as fstream:
     #SpecInput=fstream.read()
     #SpecInput.rstrip()
     #Spectrum = map(int, SpecInput.split())
    print Spectrum

    M = int(raw_input("Enter in M: "))

    print convolution(Spectrum,M)
    #for element in printList:
     #   print element, "" ,
    #print ""


if __name__== "__main__":
    main(argv)