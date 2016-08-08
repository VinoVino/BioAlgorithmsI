__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
from collections import defaultdict
import heapq

def linearSpectrum(peptide):   #peptide is provided as integer spectrum in this problem
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

def cyclicSpectrum(peptide):  #peptide is provided as integer spectrum in this problem
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

def specScore(compSpec,Spectrum):  # compare spectrum, to actual spectrum
    countCompSpectrum = Counter(compSpec)  #use counters, compare spectrum
    countSpectrum = Counter(Spectrum)      #counter, target spectrum
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
    #print sum(score), " ", peptide
    #scoreDict.update({peptide:sum(score)}) # can return dict with peptide and score

    return sum(score) #scoreDict  # can also return just score

def Expand(pList,aa):  #need to restrict masses to alfabit
  #aa=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
  i=0
  newpList = []
  while i < len (pList):
    for mass in aa:
        templist = list(pList[i])
        templist.append(mass)
        newpList.append(templist)
    i+=1

  return newpList

def Equal(peptide,spectrumCounter):
    theTruth = True
    compSpectrum = cyclicSpectrum(peptide)
    compSpectrumC = Counter(compSpectrum)
    for element in compSpectrumC:     # compare spectrums
        if compSpectrumC[element] != spectrumCounter[element]:
            theTruth = False
            break
    return theTruth

def Consistent(peptide, spectrumCounter):
    theTruth = True
    compSpectrum = linearSpectrum(peptide)   # compare spectrums
    compSpectrumC = Counter(compSpectrum)
    for element in compSpectrumC:
        if compSpectrumC[element] > spectrumCounter[element]:
            theTruth = False
            break
    return theTruth

##need to remove massDict!
def Trim(peptideList, N,Spectrum):
    trimDict=defaultdict(list)
    for peptide in peptideList:

        peptideLSpec=linearSpectrum(peptide)  #Linear spectrum
        scores= specScore(peptideLSpec,Spectrum) # score peptide vs spectrum
        trimDict[scores].append(peptide)   #add to dict

    trimScores = sorted(trimDict.keys(),reverse=True)
    returnList=list()
    for trimScore in trimScores:
        returnList.extend(trimDict[trimScore])
        if len(returnList)>N:
            break
    return returnList



def cycloPeptideSeq(Mspec,Spectrum,N):  #pass in reference spectrum and N
    spectrumC = Counter(Spectrum)
    pList=[ [] ]
    print Spectrum[-1]

    leaderPeptide=[0]
    topScore=0

    while len(pList) > 0:  ####stop it-nonempty Loop while len>0
       pList = Expand(pList,Mspec)  #updates masses to pList
       print "running Expand"
       newPlist=[]

       for peptide in pList:
            if sum(peptide) ==  Spectrum[-1]:    # if mass(peptide)=parentMass(spectrum)
                tempScore = specScore(peptide,Spectrum) # set tempscore
                print "tempScore--> ", tempScore
                if tempScore > topScore: #compare score to leaderPeptide
                    topScore=tempScore # reset topScore  ?
                    leaderPeptide=[peptide]
                elif tempScore == topScore:
                    leaderPeptide.append(peptide)  #save leaderpeptide
            if sum(peptide) < Spectrum[-1]: # compare mass spectra- if less than still continue
                #if Consistent(peptide, spectrumC): # if continue and list has a chance -shows matches- continue
                    newPlist.append(peptide)  #newPlist.append(peptide)
       newPlist=Trim(newPlist, N ,Spectrum) #trimlist to top N scores
       pList = newPlist


    finalList=[]
    for element in leaderPeptide:
        if Equal(element,spectrumC):
            finalList.append(element)

    print "final list----> ", finalList
    return leaderPeptide


def convolution(Spectrum,M):
    refSpectrum=Spectrum[:]
    tempList=[]
    for spec  in Spectrum:
        for ref in refSpectrum:
            temp=spec-ref
            if temp > 0:
                tempList.append(temp)
    finalList=[]
    for item in tempList:
        if item < 201 and item > 56:
            finalList.append(item)

    Mlist= Counter(finalList).most_common(len(finalList))
    print Mlist

    ####Return  how many confused about "include Ties means"??
    returnList=[]
    i=0
    tempCount=0
    for key,value in Mlist:
       returnList.append(key)
       if tempCount != value:
           tempCount = value
           i = i+1
       if i == M:
           break

    print "returnList "
    print len(returnList)

    return returnList


def main(argv):
    massDict={}

    input = raw_input("Enter in Seq: ")
    SpectrumUnsorted = map(int, input.split())
    Spectrum=sorted(SpectrumUnsorted)
    #with open(argv[2],"r") as fstream:
     #SpecInput=fstream.read()
     #SpecInput.rstrip()
     #Spectrum = map(int, SpecInput.split())
    #print Spectrum
    #M=int(raw_input("Enter in M: "))
    #N=int(raw_input("Enter in N: "))

    M=int(20)
    N=int(1000)

    Mspec=convolution(Spectrum,M)
    #print "Mlist returned: ", Mspec

    finalPrint = cycloPeptideSeq(Mspec,Spectrum,N)

    for element in finalPrint:
       print "-".join([str(f) for f in element]), "" ,

    print""
    print len(finalPrint)
if __name__== "__main__":
    main(argv)