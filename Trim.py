__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
import collections
import heapq

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


def specScore(compSpec,Spectrum,peptide):  # compare spectrum, to actual spectrum
    print "compSpec", compSpec
    countCompSpectrum = Counter(compSpec)
    countSpectrum = Counter(Spectrum)
    score = [] #scores
    scoreDict={} #score dict
    for cyclic in countCompSpectrum:  #for each element in cyclic
       if cyclic in countSpectrum:
            if countCompSpectrum[cyclic]== countSpectrum[cyclic]:  # equal, count either
                 score.append(countCompSpectrum[cyclic])
            elif countCompSpectrum[cyclic] > countSpectrum[cyclic]: # theoretical is greater, count Spec value
                 score.append(countSpectrum[cyclic])
            elif countCompSpectrum[cyclic] < countSpectrum[cyclic]: # spec value is greater, count theoretical
                 score.append(countCompSpectrum[cyclic])
    print sum(score), " ", peptide
    scoreDict.update({peptide:sum(score)})

    return scoreDict

def Trim(peptideList, N,Spectrum,massDict):
    trimList=[]
    trimDict={}
    for peptide in peptideList:
        peptideLSpec=linearSpectrum(peptide,massDict)    #Linear spectrum
        scores= specScore(peptideLSpec,Spectrum,peptide) # score spectrum
        trimDict.update(scores)
    print trimDict


    trimList=sorted(trimDict, key=trimDict.__getitem__, reverse=True)
    #trimList.update(heapq.nlargest(N, trimDict))
    return trimList[:N]


def main(argv):
    massDict={} #used in this problem to determine spectra


    peptideInput=raw_input("Enter in AA: ")
    peptide = map(str, peptideInput.split())

    input=raw_input("Enter spectrum: ")
    Spectrum = map(int, input.split())
    #with open(argv[2],"r") as fstream:
     # SpecInput=fstream.read()
      #SpecInput.rstrip()
    #Spectrum = map(int, SpecInput.split())

    print Spectrum

    N=int(raw_input("Enter in N: "))

    with open(argv[1],"r") as massTable:
        for line in massTable:
            line=line.rstrip()
            tokens=line.split(" ")
            aminoAcid = tokens[0]
            mass = tokens[1]
            massDict[aminoAcid]=mass


    print " ".join(Trim(peptide,N,Spectrum,massDict))

    #final = sorted (linearSpectrum(peptide,massDict))
    #score= specScore(final, Spectrum,peptide)

    #print " ".join([str(f) for f in final])
    #print "Score: ", score


if __name__== "__main__":
    main(argv)