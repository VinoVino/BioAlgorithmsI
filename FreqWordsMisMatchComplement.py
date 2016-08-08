__author__ = 'jcovino'
from sys import argv


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
    comp = [complement[base] for base in comp]   #complement from dictionary
    revComplement.append(''.join(comp))
    revComplementPrint= ("\n".join(str(e) for e in revComplement))
    return (revComplementPrint)

####################
def patternPositionCountMismatch(seq,pattern,numberMisMatch):
    match=(len(pattern)-numberMisMatch)         # of bases to match to count, takes into account mismatches
    index=0
    patternList=list(pattern)
    count=0
    print pattern
    while index < len(seq)-len(pattern)+1:               # outerloop, +1????
        curString = seq[index:index+len(pattern)]
        curStringList=list(curString)
        j=0
        matchSum=0
        while j < len(pattern):                             #search for number of matches
            if patternList[j]==curStringList[j]:
                matchSum = matchSum + 1
            j = j+1
        if matchSum >= match:                               #Determine if there is a match with mismatches
            count=count+1
        index=index+1
    return (count)

#####################
def frequentWords(seq,patternLength,numberMisMatch):
    stopLength=len(seq)-patternLength
    freqPatterns=[]
    countList=[]
    countListRVC=[]
    sumCountList=[]
    index=0
    while index < stopLength:   #outer loop
        pattern=seq[index:index + patternLength]  # define kmer
        countList.append(patternPositionCountMismatch(seq,pattern,numberMisMatch))  #count hits of kmer, function

        patternRVC=RVC(seq[index:index + patternLength]) # define RVC kmer
        countListRVC.append(patternPositionCountMismatch(seq,patternRVC,numberMisMatch)) # counts hits of RVC of kmer,function

        sumCountList.append(countList[-1]+countListRVC[-1])  # combines counts for complement and standard
        print "seq ", countList[-1]
        print "RVC", countListRVC[-1]
        print "sum", sumCountList[-1]
        print ""
        index=index+1
    print sumCountList
    maxCount=max(sumCountList)  #determine max number of hits
    print maxCount
    j=0
    while j < index:               #move through countList to determine sequence that matches max
        if sumCountList[j]== maxCount:
            freqPatterns.append(seq[j:j+patternLength])
        j=j+1
    return set(freqPatterns)



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
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G','N':'N'}

forwardList=frequentWords(seq,patternLength,numberMisMatch)

revCompList=[]

for string in forwardList:
    revCompList.append(RVC(string))
print "Pattern found forward/reverse: ", forwardList, "rev", revCompList

