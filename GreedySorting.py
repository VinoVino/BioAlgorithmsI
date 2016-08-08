__author__ = 'jcovino'
from sys import argv

"""
CODE CHALLENGE: Implement GREEDYSORTING.
     Input: A permutation P.
     Output: The sequence of permutations corresponding to applying GREEDYSORTING to P, ending with
     the identity permutation.

Sample Input:
     (-3 +4 +1 +5 -2)

Sample Output:
     (-1 -4 +3 +5 -2)
     (+1 -4 +3 +5 -2)
     (+1 +2 -5 -3 +4)
     (+1 +2 +3 +5 +4)
     (+1 +2 +3 -4 -5)
     (+1 +2 +3 +4 -5)
     (+1 +2 +3 +4 +5)

  """

def GreedySort(sequence):
    postiveSequence=[]
    # remove negative values
    for number in sequence:
        if number < 0:
            number=number*(-1)
        postiveSequence.append(number)
    #sorted sequence positive
    sortedSequence=sorted(postiveSequence)

    FinalList=[]
    CarryOver=[]

    for k in range (0,len(sequence)):

        minvalue=k+1
        minValueNeg=minvalue*-1
        if sequence[k]!=minvalue and sequence[k]!=minValueNeg:   # if element k is not in sorted order
            for i in range(0,len(sequence)):
                if sequence[i]==minvalue or sequence[i]*-1==minvalue:
                    sortindex=i
                    #print "index:",sortindex

            substring=sequence[k:sortindex+1]
            #print"substring:", substring
            substring.reverse()
            tempSubstring=[]
            for number in substring:
                tempSubstring.append(number*-1)

            #update sequence
            sequence=CarryOver+ tempSubstring+sequence[sortindex+1:]
            FinalList.append(sequence)
            #print "new sequence",sequence

            #remove negative values
            postiveSequence=[]
            for number in sequence:
                if number < 0:
                    number=number*(-1)
                postiveSequence.append(number)

            # carry over previous sorted positions in array
            CarryOver.append(sequence[k])
        else:
            CarryOver.append(sequence[k])

        if sequence[k]<0:
            tempList=sequence[:]
            tempList[k]=abs(sequence[k])
            CarryOver[k]=abs(CarryOver[k])
            FinalList.append(tempList)

    print ""
    return FinalList


def print_permutation(perm):
    return "(%s)" % ' '.join(["%+d" % e for e in perm])


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
        print "Start", sequence

        finalList=GreedySort(sequence)
        print finalList
        print len(finalList)


        outFile=open('Answer.txt','w')
        for element in finalList:
            printIt=print_permutation(element)
            print printIt
            outFile.write(printIt)
            outFile.write('\n')

        outFile.close()

if __name__== "__main__":
    main(argv)

