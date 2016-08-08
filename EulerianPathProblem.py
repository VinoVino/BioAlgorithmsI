__author__ = 'jcovino'
from sys import argv
from random import randint
from collections import defaultdict
import copy

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


def find_eulerian_path(graph):
     #
    #print vertices

    odd,ValuesLength= findOddVertices(graph) #find starting node


    print "---->>>", ValuesLength
    # Main algorithm

    Repeat=True

    while Repeat:
        vertices = copy.deepcopy(graph)
        v=[]
        randomStart=randint(0,len(odd)-1)
        Path = [odd[randomStart]] # a list starting with odd node
        print "Start", Path
        theTruth=True
        tempPath=[]
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
            print len(Path)
            print "temp", len(tempPath)

            tempPath=Path
        if len(Path)== ValuesLength+1:
            Repeat=False

    return Path



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

    graph={}
    # take in input and put in dictionary
    for element in path:
        temp= element[0].split(" -> ")
        #print temp
        graph[temp[0]]=temp[1].split(',')



    final=find_eulerian_path(graph)

    print '->'.join((final))

    outFile=open('Answer.txt','w')
    outFile.write('->'.join(final))

    outFile.close()






if __name__== "__main__":
    main(argv)

