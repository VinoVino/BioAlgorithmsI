__author__ = 'jcovino'
from sys import argv
"""Sample Input:
     5
     CAATCCAAC

Sample Output:
     AATCC
     ATCCA
     CAATC
     CCAAC
     TCCAA"""
def generateKmers(sequence,kmerLength): # generate all kmers in a given sequence
    kmers=[]
    index=0

    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        kmers.append(sequence[index:index+kmerLength])  #kmer defined
        index = index+1
    return kmers


def main(argv):


    with open(argv[1],"r") as fstream:
       kmerLength=int(fstream.readline())
       sequencesInput = fstream.read().rstrip() # rest of sequences

    print kmerLength
    print sequencesInput


    final=generateKmers(sequencesInput,kmerLength)
    finalPrint= sorted(final)

    outFile=open('Answer.txt','w')

    outFile.write ("\n".join(str(e) for e in finalPrint))
    outFile.close()





if __name__== "__main__":
    main(argv)