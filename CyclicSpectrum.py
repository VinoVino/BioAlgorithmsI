__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
from difflib import SequenceMatcher

def cyclicSpectrum(peptide,massDict):
    preFixMass=[]
    preFixMass.append(0)
    i=0
    while i < len(peptide): # generate preFixMass
        currentAA=peptide[i]
        currentMass=massDict[currentAA]
        preFixMass.append(preFixMass[i]+ int(currentMass))
        i=i+1
    peptideMass=preFixMass[(len(peptide))]
    cyclicSpec=[]
    cyclicSpec.append(0)
    k=0
    while k < len(peptide):  # subtract to generate masses of fragments
        j=k+1
        while j < len(peptide)+1:
            cyclicSpec.append(preFixMass[j]-preFixMass[k])
            if k > 0 and j < len(peptide):
                cyclicSpec.append(peptideMass-(preFixMass[j]-preFixMass[k]))
            j=j+1
        k=k+1
    return cyclicSpec
######
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

    #with open(argv[2],"r") as fstream:
     #   SpecInput=fstream.read()
      #  SpecInput.rstrip()

    SpecInput=raw_input("Enter in Spectrum: ")
    Spectrum = map(int, SpecInput.split())
    print Spectrum

    peptide=raw_input("Enter in AA: ")

    #SpecInput=input("Enter in Spectrum: ")
    #Spectrum = map(int, SpecInput.split())

    with open(argv[1],"r") as massTable:
        for line in massTable:
            line=line.rstrip()
            tokens=line.split(" ")
            aminoAcid = tokens[0]
            mass = tokens[1]
            massDict[aminoAcid]=mass


    final= sorted (cyclicSpectrum(peptide,massDict))
    print " ".join([str(f) for f in final])

    score = specScore(final,Spectrum)
    print "Score", score


if __name__== "__main__":
    main(argv)