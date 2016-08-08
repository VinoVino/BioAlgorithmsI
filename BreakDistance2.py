__author__ = 'jcovino'
__author__ = 'jcovino'
from sys import argv
import sys


"""
CODE CHALLENGE: Solve the 2-Break Distance Problem.
     Input: Genomes P and Q.
     Output: The 2-break distance d(P, Q).

Sample Input:
     (+1 +2 +3 +4 +5 +6)
     (+1 -3 -6 -5)(+2 -4)

Sample Output:
     3
"""

def ChromosomeCycle(sequence):
    finalCycle=[]

    for i in range (0, len(sequence)):
        if sequence[i]>0:
            finalCycle.append((2*sequence[i])-1)
            finalCycle.append(2*sequence[i])
        else:
            finalCycle.append(-2*sequence[i])
            finalCycle.append((-2*sequence[i])-1)
    return finalCycle

def ColoredEdges(P):
    Edges=[]
    finalEdges=[]
    for chromosome in P:
        Nodes=ChromosomeCycle(chromosome)
        #print "--->", Nodes
        for j in range (0,len(chromosome)):
            first = 2*j
            second= (2*j)+1
            Edges.append(Nodes[first-1])
            Edges.append(Nodes[second-1])
            finalEdges.append(Edges)
            Edges=[]

    return sorted(finalEdges)

def findCycles(sequence):
    Allcycles=[]
    cycles=[]
    StartEnd=[]

    startNode=sequence[0]

    cycles.append(startNode)
    i=1
    j=1
    while i < len (sequence):
        temp=[]
        if sequence[i] == startNode -1 and  i % 2==1 and i!=j:
            cycles.append(sequence[i])
            Allcycles.append(cycles)
            cycles=[]
            temp.append(startNode)
            temp.append(sequence[i])
            StartEnd.append(temp)
            if i != len(sequence)-1:
                startNode=sequence[i+1]
                i=i+1
                j=i+1

        if sequence[i] == startNode +1 and  i % 2==1 and i != j:
            cycles.append(sequence[i])
            Allcycles.append(cycles)
            cycles=[]
            temp.append(startNode)
            temp.append(sequence[i])
            StartEnd.append(temp)
            if i != len(sequence)-1:
                startNode=sequence[i+1]
                i=i+1
                j=i+1
        cycles.append(sequence[i])
        i=i+1

    #print Allcycles
    #print StartEnd
    return len(Allcycles)


def main(argv):
    with open(argv[1],"r") as fstream:
        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in fstream.readlines()]
        P = [map(int, block.split()) for block in P]
        Q = [map(int, block.split()) for block in Q]

    Blocks=0
    for element in P:
        Blocks=len(element)+Blocks
    #print "blocks", Blocks

    Pcolored=ColoredEdges(P)
    Qcolored=ColoredEdges(Q)


    PList=[]
    for element in Pcolored:
        PList.append(element[0])
        PList.append(element[1])
    #print Pcolored
    #print PList

    QList=[]
    for element in Qcolored:
        QList.append(element[0])
        QList.append(element[1])
    #print Qcolored
    #print QList

    Pcycles=findCycles(PList)
    print "Pcycles: ", Pcycles

    Qcycles=findCycles(QList)
    print "Qcycles: ", Qcycles
    print Blocks
    print "Breaking Distance: ",  Blocks-(Qcycles+Pcycles)



if __name__== "__main__":
    main(argv)
