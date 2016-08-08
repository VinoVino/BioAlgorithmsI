__author__ = 'jcovino'
from sys import argv
from random import randint
from collections import defaultdict
import copy

"""Develop EulerianPath
CODE CHALLENGE: Solve the Eulerian Path Problem.
     Input: The adjacency list of a directed graph that has an Eulerian path.
     Output: An Eulerian path in this graph.

Sample Input:
     0 -> 2
     1 -> 3
     2 -> 1
     3 -> 0,4
     6 -> 3,7
     7 -> 8
     8 -> 9
     9 -> 6

Sample Output:
     6->7->8->9->6->3->0->2->1->3->4


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
    """for element in valuesList:
        if element not in graph.keys():
            NoOutNode.append(element)
    endIndicator=['9999']
    graph.update({NoOutNode[0]:endIndicator}) ###update graph with ending node
    print "No OutNode, End ", NoOutNode"""

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



def main(argv):
    #pathsDict=defaultdict[list]
    path=[]
    temp=[]
    fileInput=[]
    with open(argv[1],"r") as fstream:
        fileInput=fstream.readlines()

    for line in fileInput:
        temp.append(line.rstrip())
        path.append(temp)
        temp=[]

    graph={}  # graph is dictionary holding node(key), nodes pointed too (values)- stored as a list
    # take in input and put in dictionary
    for element in path:
        temp= element[0].split(" -> ")
        #print temp
        graph[temp[0]]=temp[1].split(',')


    final=find_eulerian_path(graph)

    print '->'.join((final))

    #outFile=open('Answers.txt','w')
    #outFile.write('->'.join(final))
    #outFile.close()






if __name__== "__main__":
    main(argv)

