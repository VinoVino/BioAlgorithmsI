__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
from collections import defaultdict
import itertools

def mismatch(word, num_mismatches, letters='ACGT'):
    """ Provides an iterator over all words exactly num_mismatches away
        from the original word.
    http://stackoverflow.com/questions/11679855/introducing-mutations-in-a-dna-string-in-python
    :param word: input word to vary
    :type word: str
    :param num_mismatches: number of different mismatches in each result word
    :type num_mismatches: int
    :param letters: letters in the alphabet ('ACGT' would be appropriate here)
    :type letters: str
    :return: iterator, returns words with appropriate mismatches
    """

    # Loop over all combinations of locations to create a mismatch
    for locs in itertools.combinations(range(len(word)), num_mismatches):
        # Create a list of single-char lists for use in product call below
        this_word = [[char] for char in word]
        # Loop over each location and make the substitution list
        for loc in locs:
            orig_char = word[loc]
            # Replace the single char with the new options for that char in a list
            this_word[loc] = [l for l in letters if l != orig_char]
        # Calling product generates all combinations of the list elements,
        # which is pretty darn neat.
        for poss in itertools.product(*this_word):
            #print ''.join(poss)
            yield ''.join(poss)


def all_mismatches(word, max_mismatches, letters='ACGT'):
    """ Loop over max mismatches and provide mismatch results.
    :param word: input sequence to vary
    :param max_mismatches: max number of mismatches permitted
    :param letters:
    :return:
    """
    for m in range(max_mismatches+1):
        for poss in mismatch(word, m, letters):
            yield poss



def countMatch(seq,pattern,numberMisMatch):
    match=(len(pattern)-numberMisMatch)         # of bases to match to count, takes into account mismatches
    index=0
    #patternList=list(pattern)  # list of kmer
    while index < len(seq)-len(pattern)+1:               # outerloop
        curString = seq[index:index+len(pattern)] #current string in sequnce to compare
        #curStringList=list(curString)
        j=0
        matchSum=0
        while j < len(pattern):                             #search for number of matches
            if pattern[j]==curString[j]:
                matchSum = matchSum + 1
            j = j+1
        if matchSum >= match:                               #Determine if there is a match with mismatches
            return pattern
        index=index+1





def MotifFind(DNAstring,numMismatch,kmerLength): #list of DNAstrings, number of mismatches allowed, length of kmer

    finalMotifs=set()
    matchScore = kmerLength-numMismatch
    DNAdict={}

    for DNA in DNAstring:  # for sequence in list
        motifs =set()
        index=0
        kmers=[]
        while index < len(DNA)-kmerLength+1:    # generate all kmers of given length for sequence
            curString = DNA[index:index+kmerLength]
            kmers.append(list(all_mismatches(curString,numMismatch,letters='ACGT')))  # generate all possible kmer size sequences with number of mismatches
            index=index+1

        for kmer in kmers:  # check for matches in each kmer with mismatches to DNA in DNAstring
            for kmerElement in kmer:
                motifs.add(countMatch(DNA,kmerElement,numMismatch)) # add all matches to motifs list

        DNAdict[DNA]=motifs

    for element in DNAdict.values():   #intersection- use
        if len(finalMotifs) <= 0:    #first time through
            finalMotifs = element
        else:
            finalMotifs = finalMotifs.intersection(element)

    return finalMotifs



def main(argv):
    kmerLength = int(raw_input("Enter in KmerLength: "))
    num_mismatches = int(raw_input("Enter mismatches: "))

    DNAstring=[]


    with open(argv[1],"r") as fstream:
       DNAstringInput=fstream.readlines()

    for element in DNAstringInput:
        DNAstring.append(element.rstrip())
    print "input ", DNAstring

    final= (MotifFind(DNAstring,num_mismatches,kmerLength))
    print " ".join(final)
    
    print len(final)





if __name__== "__main__":
    main(argv)