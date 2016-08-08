__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter

def linearSpectrum(peptide,massDict):
    preFixMass=[]
    preFixMass.append(0)
    i=0
    while i < len(peptide): # generate preFixMass
        currentAA=peptide[i]
        currentMass=massDict[currentAA]
        preFixMass.append(preFixMass[i]+ int(currentMass))
        i=i+1
    k=0
    lspectrum=[]
    lspectrum.append(0)
    while k < len(peptide):  # subtract to generate masses of fragments
        j=k+1
        while j < len(peptide)+1:
            lspectrum.append(preFixMass[j]-preFixMass[k])
            #print preFixMass[j], " - ", preFixMass[k], " = " , lspectrum[-1]
            j=j+1
        k=k+1
    return lspectrum


def specScore(cyclicSpec,Spectrum):  # compare spectrum, to actual spectrum
    countCyclicspectrum = Counter(cyclicSpec)
    countSpectrum = Counter(Spectrum)
    score = []
    for cyclic in countCyclicspectrum:  #for each element in cyclic
       #print countCyclicspectrum[cyclic]
       if cyclic in countSpectrum:
            if countCyclicspectrum[cyclic]== countSpectrum[cyclic]:  # equal, count either
                score.append(countCyclicspectrum[cyclic])
            elif countCyclicspectrum[cyclic] > countSpectrum[cyclic]: # theoretical is greater, count Spec value
                score.append(countSpectrum[cyclic])
            elif countCyclicspectrum[cyclic] < countSpectrum[cyclic]: # spec value is greater, count theoretical
                score.append(countCyclicspectrum[cyclic])
    return sum(score)



def main(argv):
    massDict={}


    peptide=raw_input("Enter in AA: ")
    #peptidenumber=raw_input("Enter in number of AA ")

    input=raw_input("Enter spectrum: ")
    Spectrum = map(int, input.split())
    #with open(argv[2],"r") as fstream:
     #   SpecInput=fstream.read()
      #  SpecInput.rstrip()
    #Spectrum = map(int, SpecInput.split())
    print Spectrum


    with open(argv[1],"r") as massTable:
        for line in massTable:
            line=line.rstrip()
            tokens=line.split(" ")
            aminoAcid = tokens[0]
            mass = tokens[1]
            massDict[aminoAcid]=mass


    final = sorted (linearSpectrum(peptide,massDict))
    score= specScore(final, Spectrum)

    print len(final)
    print " ".join([str(f) for f in final])
    print "Score: ", score


if __name__== "__main__":
    main(argv)