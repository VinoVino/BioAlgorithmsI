__author__ = 'jcovino'
__author__ = 'jcovino'
from sys import argv
import sys


"""
ColoredEdges(P)
     Edges = an empty set
     for each chromosome Chromosome in P
          Nodes = ChromosomeToCycle(Chromosome)
          for j = 1 to |Chromosome|
               add the edge (Nodes2j, Nodes2j +1) to Edges
     return Edges


CODE CHALLENGE: Implement ColoredEdges.
     Input: A genome P.
     Output: The collection of colored edges in the genome graph of P in the form (x, y).


Sample Input:
(+1 -2 -3)(+4 +5 -6)
Sample Output:
(2, 4), (3, 6), (5, 1), (8, 9), (10, 12), (11, 7)
  """


def ColoredEdges(P):
    Edges=[]
    finalEdges=[]
    for chromosome in P:
        Nodes=ChromosomeCycle(chromosome)
        print Nodes
        for j in range (0,len(chromosome)):
            first = 2*j
            second= (2*j)+1
            Edges.append(Nodes[first-1])
            Edges.append(Nodes[second-1])
            finalEdges.append(Edges)
            Edges=[]

    #print finalEdges
    return sorted(finalEdges)

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

def print_permutation(perm):
    return "(%s)" % ', '.join(["%s" % e for e in perm])

def main(argv):
        with open(argv[1],"r") as fstream:
            sequencesInput = fstream.readlines()

        chromes=[]
        for element in sequencesInput:
            #print "--->" ,element
            # remove junk symbols
            sequence=element.replace("(","")
            sequence=sequence.replace(")","")
            sequence=sequence.replace("+","")
            sequence=sequence.split()
            #convert to int
            sequence=map(int,sequence)
            chromes.append(sequence)

        print chromes

        final=ColoredEdges(chromes)

        print ""
        print " "
        for element in final:
            print print_permutation(element),
            sys.stdout.write(', ')



        

if __name__== "__main__":
    main(argv)
