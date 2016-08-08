__author__ = 'jcovino'
from sys import argv

"""
Shared k-mers Problem: Given two strings, find all their shared k-mers.
     Input: An integer k and two strings.
     Output: All k-mers shared by these strings, in the form of ordered pairs (x, y).

CODE CHALLENGE: Solve the Shared k-mers Problem.

Sample Input:
     3
     AAACTCATC
     TTTCAAATC

Sample Output:
     (0, 4)
     (0, 0)
     (4, 2)
     (6, 6)

  """

def RVC(pattern):    #reverse complmenet function, take seq in as string(not list)
    revComplement=[]
    seqList=list(pattern)
    rev=seqList[:]
    rev.reverse()
    comp=rev[:]       # copies reversed list
    comp = [complement[base] for base in comp]   #complement from dictionary
    revComplement.append(''.join(comp))
    revComplementPrint= ("\n".join(str(e) for e in revComplement))
    return (revComplementPrint)

def generateKmers(sequence,kmerLength): # generate all kmers in a given sequence
    kmers=[]
    index=0

    while index < len(sequence)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
        kmers.append(sequence[index:index+kmerLength])  #kmer defined
        index = index+1
    return kmers

def sharekmers(seq1,seq2, kmerS1,kmerS2):
    print seq1
    print seq2
    print kmerS1
    print kmerS2

    found=[]
    for kmer in kmerS1:
        if kmer in seq2:
            found.append(kmer)

    for kmer in kmerS1:
        RVCkmer=RVC(kmer)
        if RVCkmer in seq2:
            found.append(RVCkmer)

    setFound=set(found)

    print "found", setFound
    print len(setFound)





def main(argv):
        with open(argv[1],"r") as fstream:
            kmerLength=int(fstream.readline())
            sequence1Input=fstream.readline()
            sequence2Input=fstream.readline()

            sequence1=sequence1Input.rstrip()
            sequence2=sequence2Input.rstrip()

        seq1Kmers=generateKmers(sequence1,kmerLength)
        seq2Kmers=generateKmers(sequence2,kmerLength)

        sharekmers(sequence1,sequence2,seq1Kmers,seq2Kmers)






complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G','N':'N','o':'o','e':'e','n':'n'}

if __name__== "__main__":
    main(argv)

