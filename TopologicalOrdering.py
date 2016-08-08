__author__ = 'jcovino'
from sys import  argv
from collections import defaultdict
from random import randint

"""
CODE CHALLENGE: Implement TOPOLOGICALORDERING.
     Input: The adjacency list of a graph (with nodes represented by integers).
     Output: A topological ordering of this graph.

Sample Input:
0 -> 1
1 -> 2
3 -> 1
4 -> 2

Sample Output:
0, 3, 4, 1, 2
"""
def genNumberGraph(numbersPath):
    #print numbersPath
    numberPathDict={}
    for line in numbersPath:
        tokens=line[0].split(" -> ")
        numberPathDict[tokens[0]]=tokens[1].split(',')
    return numberPathDict

def NoIncomingNodes(graph): #determine nodes with no incoming edges
    NoIncoming=[]
    valuesList=[]

    for element in graph.values():  # make one list of all the values found in the dictionary, point outward
        for subelement in element:
            valuesList.append(subelement)

    for key in graph:
        if key not in valuesList:
            NoIncoming.append(key)
    return NoIncoming

def genValuesList(graph):
    valuesList=[]
    for element in graph.values():  # make one list of all the values found in the dictionary, point outward
        for subelement in element:
            valuesList.append(subelement)
    return valuesList

def New_Topo_Ordering(graph):
    print ""
    Candidates=NoIncomingNodes(graph)
    Candidates=map(str,Candidates)
    TopoList=[]

    print graph
    print Candidates

    while len(Candidates) > 0:
        #pick=randint(0,len(Candidates)-1)
        Anode= Candidates[0]  # pick first node from cand
        if Anode not in TopoList:
            TopoList.append(Anode) # add to topolist
        del Candidates[0]  # remove item from cand

        if Anode not in graph:
            continue
        B= graph[Anode]
        del graph[Anode]
        valuesList=genValuesList(graph)
        # from each outgoing edge from Anode to another node B
        for element in B:
            print element
            if element not in valuesList:
                Candidates.append(element)

    return TopoList




def main(argv):
    print ""
    with open(argv[1], "r") as fstream:
        numbersPathInput = fstream.readlines()

    numbersPath=[]
    temp=[]
    for line in numbersPathInput:
        temp.append(line.rstrip())
        numbersPath.append(temp)
        temp=[]

    numberGraph=genNumberGraph(numbersPath)

    #final=Topo_ordering(numberGraph)
    final=New_Topo_Ordering(numberGraph)

    #final=map(int,final)
    print final
    #print ", ".join(final)
    print len(final)

if __name__== "__main__":
    main(argv)

