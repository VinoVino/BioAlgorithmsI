__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter
from collections import defaultdict
import operator
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


def hamming(seq1,seq2): #hamming distance between two strings
    seq1List=list(seq1)
    seq2List=list(seq2)
    count=0
    i=0

    while i < len(seq1):
        if seq1List[i]!= seq2List[i]:
            count=count+1
        i=i+1
    return count


def distancePatternString(pattern,sequences): #takes in pattern and list of sequences, returns minimum score (hamming distance)
    distanceDict={}                           # pattern against sequence list (mulitple sequences)
    kmerLength=len(pattern)

    for seq in sequences: # for each sequence in list
        index=0
        temp=[]
        while index < len(seq)-kmerLength+1:  # generate kmers of lenght pattern found in sequence
            curString = seq[index:index+kmerLength]    #kmer defined
            temp.append(hamming(pattern,curString))  #define and store hamming between kmer and pattern
            index = index+1
        distanceDict[seq]=min(temp) #place min value in dictionary, sequence:mininum hamming distance of pattern to sequence

    return sum(distanceDict.values())




def medainString(randomSeq,patternLength,sequences,patternDict): #determines the pattern that produces the lowest score from distancePatternString
    patternsList=[]
    patternsList.append(list(all_mismatches(randomSeq,patternLength,letters='ACGT'))) #generate all kmers
    #print patternsList
    for patterns in patternsList: #test score for each pattern against sequences
        for pattern in patterns:
            patternDict[pattern]=distancePatternString(pattern,sequences)  # place score in dictionary with key of pattern
    return patternDict



def main(argv):
    patternDict={}
    sequences=[]

    with open(argv[1],"r") as fstream:
       patternLength=int(fstream.readline())
       sequencesInput = fstream.readlines()

    for element in sequencesInput:
        sequences.append(element.rstrip())

    randomSeqwhole=sequences[0]
    randomSeq=randomSeqwhole[0:patternLength]  # randomSeq is really just a seed to create all patterns of the same length!

    print patternLength
    print randomSeq
    print sequences

    final= medainString(randomSeq,patternLength,sequences,patternDict)

    sortedfinal = sorted(final.items(), key=operator.itemgetter(1),reverse=True) # returns the dictionary sorted as a list, in reverse
    print sortedfinal  #answer is the last item with the small value

if __name__== "__main__":
    main(argv)