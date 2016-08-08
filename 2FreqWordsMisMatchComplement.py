__author__ = 'jcovino'
from sys import argv
import itertools
from collections import Counter

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



###################
def RVC(pattern):    #reverse complmenet function, take seq in as string(not list)
    revComplement=[]
    seqList=list(pattern)
    rev=seqList[:]
    rev.reverse()
    comp=rev[:]       # copies reversed list

    for element in comp:
        comp = [complement[base] for base in element]   #complement from dictionary
        revComplement.append(''.join(comp))
        revComplementPrint= ("".join(str(e) for e in revComplement))
    return (revComplementPrint)

####################
def patternPositionMismatch(seq,pattern,numberMisMatch):
    match=(len(pattern)-numberMisMatch)         # of bases to match to count, takes into account mismatches
    index=0
    #patternList=list(pattern)
    count=0

    while index < len(seq)-len(pattern)+1:               # outerloop, +1
        curString = seq[index:index+len(pattern)]
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


#####################
def frequentWords(seq,patternLength,numberMisMatch): # sequence, length of kmer, numbermismatch
    stopLength=len(seq)-patternLength+1
    kmerList=[]  # list holds all kmers that match
    kmerListRVC=[]  # list holds all rev comp kmers that match

    index=0
    while index < stopLength:   #outer loop # find each possible kmer with mismatch
        tempPattern=seq[index:index + patternLength]  # define kmer- increment through sequence
        pattern=list(all_mismatches(tempPattern,numberMisMatch,letters='ACGT')) #create all possible kmers
        for kmer in pattern:
            kmerList.append(patternPositionMismatch(seq,kmer,numberMisMatch))  #if kmer matches DNA seq put in list

            kmerRVC=RVC(kmer) # define RVC kmer
            kmerList.append(patternPositionMismatch(seq,kmerRVC,numberMisMatch)) # if RVC kmer matches DNA seq put in list
        index=index+1


    kmerListCounter=Counter(kmerList).most_common(10)  #return top ten

    return kmerListCounter



##############Main
with open(argv[1],"r") as fstream:
    seqInput=fstream.readline()
    patternLengthInput=fstream.readline()
    misMatchInput=fstream.readline()
seq=seqInput.rstrip()
patternLength=int(patternLengthInput.rstrip())
numberMisMatch=int(misMatchInput.rstrip())
print seq
print patternLength
print numberMisMatch

patternPosition=[]
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G','N':'N','o':'o','e':'e','n':'n'}

forwardList=frequentWords(seq,patternLength,numberMisMatch)


print "Pattern found forward/reverse: ", forwardList, #"rev", revCompList

