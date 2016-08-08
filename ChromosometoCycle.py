__author__ = 'jcovino'
from sys import argv

"""
CODE CHALLENGE: Implement ChromosomeToCycle.
     Input: A chromosome Chromosome containing n synteny blocks.
     Output: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle
     to Chromosome.



Sample Input:
(+1 -2 -3 +4)
Sample Output:
(1 2 4 3 6 5 7 8)
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

        final= ChromosomeCycle(sequence)


        for element in final:
            print element,





if __name__== "__main__":
    main(argv)

