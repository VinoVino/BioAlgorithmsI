__author__ = 'jcovino'
from sys import argv

"""
Number of Breakpoints Problem: Find the number of breakpoints in a permutation.
     Input: A permutation.
     Output: The number of breakpoints in this permutation.

CODE CHALLENGE: Solve the Number of Breakpoints Problem.

Sample Input:
     (+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)

Sample Output:
     8

  """

def numberBreakPoints(sequence):
     print "Start", sequence
     breakpoints=0

     if sequence[0] != 1:
         breakpoints=1

     for i in range (0, len(sequence)-1):
          if sequence[i+1] - sequence[i] != 1:
              breakpoints=breakpoints+1


     print breakpoints


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


        numberBreakPoints(sequence)




if __name__== "__main__":
    main(argv)

