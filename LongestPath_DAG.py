__author__ = 'jcovino'
from sys import  argv
from collections import defaultdict
from random import randint
import copy

import itertools

"""
CODE CHALLENGE: Solve the Longest Path in a DAG Problem.
     Input: An integer representing the source node of a graph, followed by an integer representing the
     sink node of the graph, followed by a list of edges in the graph. The edge notation 0->1:7 indicates
     that an edge connects node 0 to node 1 with weight 7.
     Output: The length of a longest path in the graph, followed by a longest path.

Sample Input:
     0
     4
     0->1:7
     0->2:4
     2->3:2
     1->4:1
     3->4:3

Sample Output:
     9
     0->2->3->4
"""
def genNumberGraph(numbersPath):  # generate graphs, weighted and unweighted
    weightPathDict={}  #keys are nodes: 1,2 (1 to 2), value needs to be weight-- directed graph
    pathDict=defaultdict(list)
    # key is start node, value[0]-> node, value[1]- weight to travel to node
    for line in numbersPath:
        tokens=line[0].split("->")
        weight=tokens[1].split(":")
        weightPathDict[tokens[0]+"-"+weight[0]]=int(weight[1])
        pathDict[tokens[0]].append(weight[0])
    return weightPathDict,pathDict


def thePath_SourcetoSink(graphInput,sourceNode,sinkNode):  #function to find 'all' paths that start at source and end at sink
    PathsFound=[]
    i=0

    while i < 50:
        graph=copy.deepcopy(graphInput)
        v=[]
        Path=[]
        Path.append(str(sourceNode))
        theTruth=True
        while theTruth:
            v = Path[-1] # select the starting vertex
            if v not in graph or v==str(sinkNode):  #if end is found
                theTruth=False
                break
            if graph[v]: # if there are unused edges from the starting vertex
                spot=0
                if len(graph[v]) > 1:
                    spot=randint(0,len(graph[v])-1)
                w = graph[v][spot] # select the vertex connected, if more than one connection-pick at random
                Path.append(w) # add the new vertex to the stack, to become the new starting vertex
                # delete edge v-w from the graph
                del graph[v][spot]
        i=i+1
        if Path[-1]==str(sinkNode):
            PathsFound.append(Path)

    b_set = set(tuple(x) for x in PathsFound)
    Unique_PathsFound = [ list(x) for x in b_set ]

    #print PathsFound
    return Unique_PathsFound

def ScoreGraph(Unique_Paths,weightPath ): # function determines total weight of paths that start at source and end at sink

    scoreMe=[]
    finalPath=0
    print "Unique Paths-", Unique_Paths

    for list in Unique_Paths:
        i=0
        tempList=[]
        while i < len(list)-1 :
            tempList.append(list[i])
            tempList.append(list[i+1])
            if tempList not in scoreMe:
                scoreMe.append(tempList)
            i=i+1
        for paths in scoreMe:
            totalScore=0
            i=0
            while i < len(paths)-1:
                score=str(paths[i])+"-"+str(paths[i+1])
                intScore= weightPath[score]
                totalScore=totalScore+intScore
                i=i+2

        print totalScore
        print "->".join(list)
        print ""


def main(argv):
    print ""
    with open(argv[1], "r") as fstream:
        sourceNode=int(fstream.readline())    ##starting node
        sinkNode=int(fstream.readline())      ## ending node
        numbersPathInput = fstream.readlines()
    numbersPath=[]
    temp=[]
    for line in numbersPathInput:
        temp.append(line.rstrip())
        numbersPath.append(temp)
        temp=[]

    weightPath, graph =genNumberGraph(numbersPath)  # generate graph

    #print weightPath
    #print graph


    Unique_Paths= thePath_SourcetoSink(graph,sourceNode,sinkNode)

    ScoreGraph(Unique_Paths,weightPath)


if __name__== "__main__":
    main(argv)

