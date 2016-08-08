#!/usr/bin/env python

__author__ = 'jcovino'

import fileinput
f=open('Reverse_Complement.txt','w')
sequence=[]
reversed=[]
revComplement=[]
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}


#####Function
def RVC(seq):    #reverse complmenet function
    rev=seq[:]     #copies sequence list
    rev.reverse()
    comp=rev[:]        # copies reversed list
    comp = [complement[base] for base in comp]   #complement from dictionary
    revComplement.append(''.join(comp))
    #sequence.append(''.join(seq))
    #reversed.append(''.join(rev))
    f.write ("\n".join(str(e) for e in revComplement))
    revComplementPrint= ("\n".join(str(e) for e in revComplement))
    return revComplementPrint

for line in fileinput.input():
    upped=line.upper()
    seq=list(upped.rstrip())
    print "Reverse Complement: ",RVC(seq)

#print "Original Sequence"
#print sequence
#print "Reversed Sequence"
#print reversed






f.close()




                