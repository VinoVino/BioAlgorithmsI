__author__ = 'jcovino'
from sys import argv
from random import randint
from collections import defaultdict
import copy

"""
Sample Input:
     4
     CTTA
     ACCA
     TACC
     GGCT
     GCTT
     TTAC

Sample Output:
     GGCTTACCA
CODE CHALLENGE: Solve the String Reconstruction Problem.
     Input: An integer k followed by a list of k-mers Patterns.
     Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may
     return any one.)

"""



def dsum(*dicts):
    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)


def findOddVertices(graph):
    Out= {}
    In= {}
    oddVertices=[]
    NoOutNode=[]
    valuesList=[]

    for element in graph.values():  # make one list of all the values found in the dictionary
        for subelement in element:
            valuesList.append(subelement)

    ValuesLength=len(valuesList)

    #determine number of -> for each key, pointint outward---Out
    for key,value in graph.items():
        Out[key]=len(value)

    # determine number of <- values pointing toward key---IN
    tempcount=0
    for key in graph.keys():
        #print "key", key
        for element in valuesList:
            if key == element:
                tempcount=tempcount+1
        In[key]=tempcount
        tempcount=0

    SumInOut= dsum(In,Out)
    #print "Sum In and Out- ", SumInOut

    for key,value in SumInOut.items():
        if value % 2 != 0:
            oddVertices.append(key)
    print "odd vertices, start ", oddVertices

    #determine if number doesn't point to any node at all (ending)

    return oddVertices,ValuesLength

def eulerianPath_OneWayExit(vertices,ValuesLength,odd): # if there is one item in odd list, with the second odd item being a one way exit -> (value points to no keys)
    Repeat=True
    while Repeat:
        v=[]
        Path = [odd[0]] # a list starting with odd node
        theTruth=True
        while theTruth:
            v = Path[-1] # select the starting vertex
            if v not in vertices:  #if end is found
                theTruth=False
                break
            if vertices[v]: # if there are unused edges from the starting vertex
                spot=0
                if len(vertices[v]) > 1:
                    spot=randint(0,len(vertices[v])-1)
                w = vertices[v][spot] # select the vertex connected, if more than one connection-pick at random
                Path.append(w) # add the new vertex to the stack, to become the new starting vertex
                # delete edge v-w from the graph
                del vertices[v][spot]
        if len(Path)== ValuesLength+1:
            Repeat=False

        return Path

def find_eulerian_path(graph):
     #
    #print vertices

    odd,ValuesLength= findOddVertices(graph) #find starting node

    # Main algorithm

    if len(odd)<2:  # if only one odd element in list, ending is one way->
        vertices = copy.deepcopy(graph)
        return eulerianPath_OneWayExit(vertices,ValuesLength,odd)

    else:  # if there is two elements in odd list
        Tour=[]
        Repeat=True
        print graph
        while Repeat:
            vertices = copy.deepcopy(graph)
            v=[]
            randomStart=randint(0,len(odd)-1)
            Path = [odd[randomStart]] # a list starting with odd node

            while Path:
                v = Path[-1] # select the starting vertex
                #if str(v) not in graph.keys():  #if end is found
                    #Tour=Path
                    #print "1 way end"

                if vertices[v]: # if there are unused edges from the starting vertex
                    spot=0
                    if len(vertices[v]) > 1:
                        spot=randint(0,len(vertices[v])-1)
                    w = vertices[v][spot] # select the vertex connected, if more than one connection-pick at random
                    Path.append(w) # add the new vertex to the stack, to become the new starting vertex
                    # delete edge v-w from the graph
                    del vertices[v][spot]
                else:
                    Tour.append(Path.pop())
                #print Tour

            if len(Tour)== ValuesLength+1:
                Repeat=False

        finalrev=reversed(Tour)

    return finalrev


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


def genomePath(seq): # returns single string from a collection of kmers with overlap
    print "here"
    sequences=copy.deepcopy(seq)

    sequenceStart=sequences[0]
    del sequences[0]

    finalSeq=str(sequenceStart)

    for seq in sequences:
        concate=str(seq[-1])
        finalSeq=finalSeq + concate
    print len(finalSeq)
    return finalSeq



def main(argv):

    fileInput=[]
    kmers=[]
    graph={}
    with open(argv[1],"r") as fstream:
        kmerLength=int(fstream.readline())
        KmerInput=fstream.readlines()

    for line in KmerInput:
        kmers.append(line.rstrip())

    print kmerLength
    print kmers
    graph= deBrujin(kmers)

    print graph


    path=find_eulerian_path(graph)
    print "path---", path
    print genomePath(path)



    #outFile=open('Answers.txt','w')
    #outFile.write('->'.join(final))
    #outFile.close()






if __name__== "__main__":
    main(argv)


