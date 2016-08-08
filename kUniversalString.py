__author__ = 'jcovino'
from sys import argv
from random import randint
from collections import defaultdict
import copy
import itertools
from collections import Counter

"""
CODE CHALLENGE: Solve the k-Universal Circular String Problem.
     Input: An integer k.
     Output: A k-universal circular string.

Sample Input:
     4

Sample Output:
     0000110010111101"""



def suffix(seq):
    suffixSeq=seq[1:]
    #print "suffix ", suffixSeq
    return suffixSeq

def preFix(seq):
    preFixSeq=seq[:len(seq)-1]
    #print "prefFix ", preFixSeq
    return preFixSeq

def deBrujin(kmers): # put kmers into graph dictionary using prefix and suffix
    matchList=defaultdict(list)

    for kmer in kmers:
        matchList[preFix(kmer)].append(suffix(kmer))

    return matchList


def genomePath(seq): # returns single string from a collection of kmers with overlap
    sequences=copy.deepcopy(seq)
    sequenceStart=sequences[0]
    del sequences[0]

    finalSeq=str(sequenceStart)

    for seq in sequences:
        concate=str(seq[-1])
        finalSeq=finalSeq + concate

    return finalSeq

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

def find_eulerian_tour(graph): # euluerian cycle problem
    vertices = graph
    stack=[]
    #maxGraph=max(graph.keys(), key=int)
    #start_vertex=randint(0,int(maxGraph)-2)
    # Choose a starting vertex v and follow a trail of edges from that vertex until returning to v.
    stack.append(vertices.keys()[3])


    tour = [] # a list containing the final tour

    while stack:
        v = stack[-1] # select the starting vertex
        if vertices[v]: # if there are unused edges from the starting vertex
            w = vertices[v][0] # select the vertex connected by the first unused edge
            stack.append(w) # add the new vertex to the stack, to become the new starting vertex
            del vertices[v][0]    # delete edge v-w from the graph
        else:
            # if there are no unused edges from the starting vertex, remove it from the stack
            # and add it to the final tour
            tour.append(stack.pop())
    print "--------------------------"
    return tour




def main(argv):
        seqLength=int(raw_input("Enter in seq Length : "))
        word= str(seqLength*'0')
        print word

        allKmers= list(all_mismatches(word,int(seqLength),letters='01'))

        print allKmers
        graph= deBrujin(allKmers)
        print graph
        tour= find_eulerian_tour(graph)
        #print '->'.join(tour)
        #how to make circular????????

        #print tour

        tour.reverse()
        print tour
        final= genomePath(tour[:-seqLength+1])
        print len(final)
        print "circular", final

        nonCircular=genomePath(tour)
        print "linear", nonCircular
if __name__== "__main__":
    main(argv)

