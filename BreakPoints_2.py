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

def breakpoint_count(permutation):
    '''Returns the number of breakpoints in a given permutation.'''

    # Prepend 0 and append len(permutation)+1 to check if the endpoints are in place.
    return sum(map(lambda x,y: x - y != 1, permutation+[len(permutation)+1], [0]+permutation))



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


        print breakpoint_count(sequence)




if __name__== "__main__":
    main(argv)

