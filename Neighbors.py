__author__ = 'jcovino'


pattern=raw_input("Pattern: ")
d=raw_input("D: ")




def Neighbors(pattern,d):
    if d == 0:
        return pattern
    if len(pattern)==1:
        return

