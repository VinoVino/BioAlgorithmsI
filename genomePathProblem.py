__author__ = 'jcovino'
from sys import argv

# reconstruct final string given overlapping kmers
"""
Sample Input:
ACCGA
CCGAA
CGAAG
GAAGC
AAGCT
Sample Output:
ACCGAAGCT"""

def genomePath(sequenceStart,sequences):
    finalSeq=str(sequenceStart)

    for seq in sequences:
        concate=str(seq[-1])
        finalSeq=finalSeq + concate

    return finalSeq


def main(argv):

    sequences=[]
    with open(argv[1],"r") as fstream:
       sequenceStart=fstream.readline().rstrip()
       sequencesInput = fstream.readlines() # rest of sequences

    for element in sequencesInput:
        sequences.append(element.rstrip())
    print sequenceStart
    print sequences



    print genomePath(sequenceStart,sequences)







if __name__== "__main__":
    main(argv)