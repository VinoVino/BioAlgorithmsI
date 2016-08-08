__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter

def linearSpectrum(peptide):
    preFixMass=[]
    preFixMass.append(0)
    i=0
    while i < len(peptide): # generate preFixMass
        currentMass=peptide[i]
        preFixMass.append(preFixMass[i]+ int(currentMass))
        i=i+1
    k=0
    lspectrum=[]
    lspectrum.append(0)
    while k < len(peptide):  # subtract to generate masses of fragments
        j=k+1
        while j < len(peptide)+1:
            lspectrum.append(preFixMass[j]-preFixMass[k])
            j=j+1
        k=k+1
    return lspectrum

def cyclicSpectrum(peptide):
    preFixMass=[]
    preFixMass.append(0)
    i=0
    while i < len(peptide): # generate preFixMass
        currentMass=peptide[i]
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
    return sorted(cyclicSpec)


def Expand(pList):
  aa=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
  i=0
  newpList = []
  while i < len (pList):
    for mass in aa:
        templist = list(pList[i])
        templist.append(mass)
        newpList.append(templist)
    i+=1
  print "running Expand "
  return newpList

def Equal(peptide,spectrumCounter):
    theTruth = True
    compSpectrum = cyclicSpectrum(peptide)             # compare spectrums, comparing to cyclicSpectrum???-ok
    compSpectrumC = Counter(compSpectrum)
    for element in compSpectrumC:     # compare spectrums
        if compSpectrumC[element] != spectrumCounter[element]:
            theTruth = False
            break
    return theTruth

def Consistent(peptide, spectrumCounter):
    theTruth = True
    compSpectrum = linearSpectrum(peptide)   # compare spectrums, compare to linearSpectrum!
    compSpectrumC = Counter(compSpectrum)
    for element in compSpectrumC:
        if compSpectrumC[element] > spectrumCounter[element]:
            theTruth = False
            break
    return theTruth

def cycloPeptideSeq(Spectrum):

    print  "total mass" , Spectrum[-1]
    spectrumC = Counter(Spectrum)
    pList=[ [] ]

    Final=[]
    j=0
    while len(pList) > 0:  ####stop it-nonempty Loop while len>0
       pList = Expand(pList)
       print pList
       newPlist=[]
       for peptide in pList:

            if sum(peptide) == Spectrum[-1]:    # if mass(peptide)=parentMass(spectrum)
                if Equal(peptide,spectrumC): # compare sepctra
                    Final.append(peptide)  #save into final list
                    continue
                    # print "Match"
            if sum(peptide) < Spectrum[-1]:
                if Consistent(peptide, spectrumC):
                    # print "Consistent"
                    newPlist.append(peptide)

       pList = newPlist

    return Final


def main(argv):
    massDict={}

    #with open(argv[2],"r") as fstream:
    #   SpectrumInitial=fstream.read()
    #SpectrumInitial.rstrip()
    #for i in range(len(SpectrumInitial)):
    #   Spectrum.append(SpectrumInitial[i])


    input=raw_input("Enter spectrum: ")
    Spectrum = map(int, input.split())


    with open(argv[1],"r") as massTable:
        for line in massTable:
            line=line.rstrip()
            tokens=line.split(" ")
            aminoAcid = tokens[0]
            mass = tokens[1]
            massDict[aminoAcid]=mass


    finalPrint= (cycloPeptideSeq(Spectrum))

    for element in finalPrint:
        print "-".join([str(f) for f in element]), "" ,






if __name__== "__main__":
    main(argv)