__author__ = 'jcovino'

from sys import argv
from collections import defaultdict
import itertools
import copy
"""
Sample Input:
     ATG
     ATG
     TGT
     TGG
     CAT
     GGA
     GAT
     AGA

Sample Output:
     AGA
     ATG
     ATG
     CAT
     GAT
     TGGA
     TGT
"""
def dsum(*dicts):
    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)

def findOddVertices(graph): #determine odd vertices (unbalanced nodes)---updated to include unbalance of in and out 1-1, greater than that and included odd, even if balanced
    Out= {}
    In= {}
    oddVertices=[]
    valuesList=[]

    for element in graph.values():  # make one list of all the values found in the dictionary
        for subelement in element:
            valuesList.append(subelement)

    #determine number of -> for each key, pointint outward---Out
    for key,value in graph.items():
        Out[key]=len(value)

    # determine number of <- values pointing toward key---IN
    tempcount=0
    for key in graph.keys():
        for element in valuesList:
            if key == element:
                tempcount=tempcount+1
        In[key]=tempcount
        tempcount=0

    SumInOut= dsum(In,Out)

    for key,value in SumInOut.items():
        if value % 2 != 0:
            oddVertices.append(key)
        if value > 2:
            oddVertices.append(key)


    oddVertices=set(oddVertices)

    return oddVertices


def findCycles(graph): # find out if there are cycles in the supplied graph####this step is broken
    potentialCycle=[] # list storing potential cycle starting elemnents- balanced nodes- not odd

    oddVertices=findOddVertices(graph)
    #oddVertices=map(int,oddVertices)
    #oddVertices.sort()
    #oddVertices=map(str,oddVertices)

    for key in graph:
        if key not in oddVertices:  # potentail cycles don't have odd start sites
            potentialCycle.append(key)

    cycle=[]
    temp=['!']
    cycle.append(temp)


    for Start in potentialCycle: # start is key value from graph that has potential of being a cycle
        tempPath = []
        tempPath.append(Start)
        theTruth=True
        addtoCycle=True

        # check to see if we are searching in pre-existing/found loop, if cycle is redudant


        while theTruth:  # 1) while start of list != end of list, 2) while fork not reached, 3) while not dead end
            nextNode = graph[Start] # select the next connect node
            nextNodeKey=nextNode[0]
            tempPath.append(nextNodeKey)

            if nextNodeKey not in graph:  # while not deadend
                theTruth=False
                break

            if len(graph[nextNodeKey]) > 1:  # break
                theTruth=False
                break

            Start=nextNodeKey
            currentNode=tempPath[-1]

            if tempPath[0]==currentNode:  # if start = end, end we've found the cycle
                nextNode=graph[currentNode]
                lastnode=nextNode[0]
                theTruth=False

                for list in cycle:  # if loop /different order was already added, don't add again!
                    for element in list:
                        if element in tempPath:
                            addtoCycle=False
                if addtoCycle:
                    cycle.append(tempPath)

    return cycle



def maxNonBranchingPath(graph):
    odd = findOddVertices(graph) #find starting node
    nonBranching=[]

    #odd = map(int, odd)
    #odd.sort()
    #odd=map(str,odd)

    print "odd ", odd

    for oddStart in odd:  #outerloop, for every oddStart site
        tempPath=[]
        splitPath=[]

        nextNodeOddCheck=graph[oddStart]
        #print "---", nextNodeOddCheck

        if len(nextNodeOddCheck) > 1:           # loop to handle odd nodes with more than 1 outward node
            theTruth=True
            tempPath.append(oddStart)  #start path
            splitPath.append(oddStart) #start path in another list

            nextNode=graph[oddStart] # move to next node

            nextNodeKey=nextNode[0]
            splitNodeKey=nextNode[1]

            splitPath.append(splitNodeKey)
            #print "split path", splitPath


            while splitPath[-1] != tempPath[-1]:  #build tempPath as long as 1)it doesn't split again, 2) ends 3) or reaches the split path splitNodekey
                tempPath.append(nextNodeKey)
                if nextNodeKey not in graph:  #if reached deadend, break
                    break

                nextNode=graph[nextNodeKey]
                nextNodeKey=nextNode[0]

                if len(graph[nextNodeKey]) >1:  # if fork is reached, break
                    break

        else:
            while len(graph[oddStart])== 1:       # loop to handle odd nodes with only 1 outward path
                tempPath.append(oddStart)  #add element to list
                nextNode=graph[oddStart]  #next start site
                nextNodeKey=nextNode[0]  #put into non list
                oddStart=nextNodeKey  #allow for movement of nextnode at start of loop
                if nextNodeKey not in graph:
                    print "!!!!"
                    tempPath.append(nextNodeKey)
                    break
                if len(graph[oddStart])>1:
                    tempPath.append(nextNodeKey)  # add last element


        nonBranching.append(tempPath)
        nonBranching.append(splitPath)

        nonBranchingTrimmed = [x for x in nonBranching if x != []]  # remove any []


    return nonBranchingTrimmed





def genNumberGraph(numbersPath):
    #print numbersPath
    numberPathDict={}
    for line in numbersPath:
        tokens=line[0].split(" -> ")
        numberPathDict[tokens[0]]=tokens[1].split(',')
    return numberPathDict

def genomePath(sequences):
    finalSeq=str(sequences[0])
    for seq in sequences[1:]:
        concate=str(seq[-1])
        finalSeq=finalSeq + concate

    return finalSeq

def suffix(seq):
    suffixSeq=seq[1:]
    #print "suffix ", suffixSeq
    return suffixSeq

def preFix(seq):
    preFixSeq=seq[:len(seq)-1]
    #print "prefFix ", preFixSeq
    return preFixSeq

def deBrujin(kmers): # put kmers into graph dictionary using prefix and suffix
    matchList=defaultdict(list)
    for kmer in kmers:
        matchList[preFix(kmer)].append(suffix(kmer))
    return matchList


def main(argv):
    kmers=[]
    with open(argv[1],"r") as fstream:
        KmerInput=fstream.readlines()


    for line in KmerInput:
        kmers.append(line.rstrip())

    #266 example length
    graph=deBrujin(kmers)

    print graph
    cycles=findCycles(graph)
    path=maxNonBranchingPath(graph)


    print path
    #print len(path)
    #print cycles
    final=[]
    print""
    print"---------"
    for element in path:
       final.append(genomePath(element))

    for item in final:
        print item


    print len(final)

if __name__== "__main__":
    main(argv)