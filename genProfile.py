__author__ = 'jcovino'
from sys import argv



def genProfile(kmers):
    Ascores=[]
    Cscores=[]
    Gscores=[]
    Tscores=[]


    for i in range (len(kmers[0])): # for length of kmer list, number of kmers
        Acount=0       # reset counts for A, C, G ,T
        Ccount=0
        Gcount=0
        Tcount=0
        Ascores.append(0)
        Cscores.append(0)
        Gscores.append(0)
        Tscores.append(0)
        for kmer in kmers:
            if kmer[i] == 'A':
                Acount=Acount+1
            elif kmer[i]== 'C':
                Ccount=Ccount+1
            elif kmer[i]=='G':
                Gcount=Gcount+1
            else:
                Tcount=Tcount+1

            sumNucleotides= float(len(kmers))
            #print Acount/sumNucleotides
            Ascores[i] = float(Acount/sumNucleotides)
            Cscores[i] = float(Ccount/sumNucleotides)
            Gscores[i] = float(Gcount/sumNucleotides)
            Tscores[i] = float(Tcount/sumNucleotides)

    return Ascores, Cscores, Gscores, Tscores



def main(argv):

    kmers=['GGC','AAG']


    print genProfile(kmers)


   # Inputs dna: a collection of Strings, all of the same length
   # k: the length of the motifs/kmers to find
   # t: the number of Strings in Dna


if __name__== "__main__":
    main(argv)

