__author__ = 'jcovino'
from sys import argv

"""
CODE CHALLENGE: Implement CycleToChromosome.
     Input: A sequence Nodes of integers between 1 and 2n.
     Output: The chromosome Chromosome containing n synteny blocks resulting from applying
     CycleToChromosome to Nodes.

Sample Input:
(1 2 4 3 6 5 7 8)

Sample Output:
(+1 -2 -3 +4)

PseudoCode:

  CycleToChromosome(Nodes)
     for j = len( 1 to Nodes)/2
          if Node2j-1 < Node2j              # 1st node < second node
               Chromosomej = Node(2j) /2
          else
               Chromosomej = -Node(2j-1)/2
     return Chromosome

  """


def CycleToChrome(node):
    print node
    Chromosome=[]
    stopLength= (len(node)/2)



    for i in range (0, len(node)-1,2):
        print i
        if node[i] < node[i+1]:       # 1st node < second node
            print "top"
            Chromosome.append(node[i+1]/2)
        else:
            print "-->",node[i]
            Chromosome.append(-1* node[i]/2)
            print "--bottom"
        print ""

    return Chromosome

def print_permutation(perm):
    return "(%s)" % ' '.join(["%+d" % e for e in perm])

def main(argv):
        with open(argv[1],"r") as fstream:
            sequencesInput = fstream.readline()
        # remove junk symbols
        sequence=sequencesInput.replace("(","")
        sequence=sequence.replace(")","")
        sequence=sequence.replace("+","")
        sequence=sequence.split()
        #convert to int
        sequence=map(int,sequence)

        final=CycleToChrome(sequence)

        print print_permutation(final)


if __name__== "__main__":
    main(argv)

