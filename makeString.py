__author__ = 'jcovino'
from sys import argv

def main(argv):
    seq=[]

    with open(argv[1],"r") as fstream:
        seq=fstream.read()


    #seq.strip()

    outFile=open('bBrevisString.txt','w')
    outFile.write (seq)
    outFile.close()



if __name__== "__main__":
    main(argv)