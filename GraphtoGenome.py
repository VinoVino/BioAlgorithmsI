__author__ = 'jcovino'
__author__ = 'jcovino'
from sys import argv
import sys


"""

GraphToGenome(GenomeGraph)
     P = an empty set of chromosomes
     for each cycle Nodes in GenomeGraph
          Chromosome = CycleToChromosome(Nodes)
          add Chromosome to P
     return P


CODE CHALLENGE: Implement GraphToGenome.
     Input: The colored edges ColoredEdges of a genome graph.
     Output: The genome P corresponding to this genome graph.

     Sample Input:
(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)
Sample Output:
(+1 -2 -3)(-4 +5 -6)
  """


def CycleToNumber(node,length,startnumber):
    #print node
    numberChrome=[]
    for j in range (0,length,2):
        numberChrome.append(startnumber)
        startnumber=startnumber+1

    Chromosome=[]
    #first node
    if node[-1] > node[0]:
        numberChrome[0]=numberChrome[0]*-1

    j=1
    for i in range (1, length-2,2):
        #print node[i], node[i+1]
        if node[i] > node[i+1]:
            numberChrome[j]=numberChrome[j] *-1
        j=j+1

    print numberChrome
    return numberChrome


def findCycles(sequence):

    print "---", sequence
    #print "sequences", sequence
    Allcycles=[]
    cycles=[]

    startNode=sequence[0]

    cycles.append(startNode)
    i=1
    j=1
    while i < len (sequence):
        if sequence[i] == startNode -1 and  i % 2==1 and i!=j:
            cycles.append(sequence[i])
            Allcycles.append(cycles)
            cycles=[]
            if i != len(sequence)-1:
                startNode=sequence[i+1]
                i=i+1
                j=i+1
        if sequence[i] == startNode +1 and  i % 2==1 and i != j:
            cycles.append(sequence[i])
            Allcycles.append(cycles)
            cycles=[]
            if i != len(sequence)-1:
                startNode=sequence[i+1]
                i=i+1
                j=i+1
        cycles.append(sequence[i])
        i=i+1


    #print "allcycles:", Allcycles

    genomes=[]
    startnumber=1
    for element in Allcycles:
        #print element, "000"
        length=len(element)
        #print "startnumber", startnumber
        genomes.append(CycleToNumber(element,length,startnumber))
        startnumber=startnumber+length/2

    return genomes

def print_permutation(perm):
    return "(%s)" % ' '.join(["%+d" % e for e in perm])


def main(argv):
        with open(argv[1],"r") as fstream:
            sequencesInput = fstream.readline()
        # remove junk symbols
        sequence=sequencesInput.replace("(","")
        sequence=sequence.replace(")","")
        sequence=sequence.replace("+","")
        sequence=sequence.replace(",","")
        sequence=sequence.split()
        #convert to int
        sequence=map(int,sequence)

        print "len/2----", len(sequence)/2
        final=findCycles(sequence)
        print ""
        print ""
        for element in final:
            print print_permutation(element),


        

if __name__== "__main__":
    main(argv)
