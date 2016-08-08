__author__ = 'jcovino'
from sys import  argv
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
from Bio.SubsMat import MatrixInfo as matlist

"""
  Input: Two protein strings written in the single-letter amino acid alphabet.
     Output: The maximum alignment score of these strings followed by an alignment achieving this
     maximum score. Use the BLOSUM62 scoring matrix and indel penalty sigma = 5.


Sample Input:
     PLEASANTLY
     MEANLY

Sample Output:
     8
     PLEASANTLY
     -MEA--N-LY
"""

def score_match(pair, matrix):
    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]

def score_pairwise(seq1, seq2, matrix, gap_s, gap_e):
    score = 0
    gap = False
    for i in range(len(seq1)):
        pair = (seq1[i], seq2[i])
        if not gap:
            if '-' in pair:
                gap = True
                score += gap_s
            else:
                score += score_match(pair, matrix)
        else:
            if '-' not in pair:
                gap = False
                score += score_match(pair, matrix)
            else:
                score += gap_e
    return score


def main(argv):
    with open(argv[1], "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print sequence1
    print"---"
    print sequence2

    alignments=[]
    matrix = matlist.blosum62

    for a in pairwise2.align.globalds(sequence1, sequence2,matrix,-5,-5):
         print(format_alignment(*a))
         alignments.append(a)

    print matrix

    #print "--->", alignments
    blosum = MatrixInfo.blosum62
    """
    scores=[]
    for align in alignments:
        seq1=align[0]
        seq2=align[1]
        currentScore=score_pairwise(seq1, seq2, blosum, -5, -5)
        #print currentScore
        scores.append(currentScore)
        #print seq1
        #print seq2
        #print ""
    print "max", max(scores)
    """
    #print "---correct score: ", score_pairwise('ILYPRQSMICMSFCF-WDM--WKKDVPVVLMMFLERRQMQSVF-S-WL--VTVKTDCGKGIYNHR-K--Y-LGLPTMTAGDWHWIKK---Q-NDPHEWFQGRLETAWLHSTFLYWKYFE-CDAVKVCMDTFGLFGHCDWDQQIHTCTHENEPAIAFLDLYCRHSPMCDKLYPVWDMACQTCHFHHSWFCRNQEMWMKGDVDDWQWGYHYHTINSAQCNQWFKEICKDMGWDSVFPPRHNCQRHKKCMPALYAGIW---MA----TDHACTFMVRLIYTENIAEWHQVYCYRSMNMFTCGNVCLRCKSWIFVKN-YMMAPVVNDPMIEA--FYKRCCILGKAWYDMWGICPVERKSHWEIYAKDLLSFESCCSQKKQNCYTDNWGLEYRLFFQSIQMN-TDPH----Y--CQTHVCW-ISAMF-PIYSPFYT--SG-PKEFYMW---LQARI-DQNM---HGHANHYV-TSGNWDSVYTPEKRA--G--V-FP-V-V-------VPVWYPPQMCN--D-YIKLTYEC--E---RFHVEGTFGCNRWD-L-GCRR--YII--FQCPYCDTMKI---CY--VDQWRSIKEGQFRMSGYPNHGYWFVHDDHTNEW-----CNQPVLAKFVRSKIVA---ICKKSQTVFHYAYTPGYNATWPQTNVCERMYGPHDNLLNNQQNVTFWWKMVPNCGMQILISCHNKMKWPT--S-HYVF---MRLKCMHVLMQMEYLDHFTGPGEGDFCRNMQPYMHQDLHWEGSMRAILEYQAEHH-RRAFRA----ELCAQYDQEIILWSGGWGVQDCGFHANYDGSLQVVSGEPCSMWCTTVMQYYADCWEKCMFA', 'ILIPRQQMGCFPFPWHFDFCFWSAHHSLVVP--LNP-QMQTVFQNRGLDRVTVKTDC----HDHRWKWIYNLGLPTMTAGDWHFIKKHVVRANNPHQWFQGRLTTAWLHSTFLY-KKTEYC-LVR---HS-NCC-HCDWDQIIHTCAF-----IAFLDLYQRHWPMCDKLY------C---HFHHSWFCRNQEMSM--D---W---------N--Q---WFP-------WDSV-P-RANCLE-EGALIALYAGIWANSMKRDMKTDHACT--VRLIYVCELHAWLK-YCYTSINML-CGNVCLRCKSWIFVKLFYMYAPVVNTIEANSPHYYKRCCILGQ------GICPVERKSHCEIYAKDLLSFESCCSQK-QNCYTDNWGLEYRLFFQHIQMECTDPHANRGWTSCQTAKYWHFNLDDRPP-KEFYMWLQATPTDLCMYQHCLMFKIVKQNFRKQHGHANPAASTSGNWDSVYTPEKMAYKDWYVSHPPVDMRRNGSKMVPVWYPPGIWHWKQSY-KLTYECFFTVPGRFHVEGTFGCNRWDHQPGTRRDRQANHQFQCPYSDTMAIWEHAYTYVDQWRSIKEGQMPMSGYPNHGQWNVHDDHTNEQERSPICNQPVLAKFVRSKNVSNHEICKKSQTVFHWA-C---EA---QTNVCERMLN-NQHVAV-KRNVTFWWQMVPNC----LWSCHNKMTWPTRPEQHRLFFVKMRLKCMH-----EYLD--VAPS--DFCRNMQAYMH-------SMRAILEYQADFDLKRRLRAIAPMDLCAQYDQEIILWSGGY-I--------YDQSLQVVSCEGCSYYADCYVKCI-NVKEKCMFA', blosum, -5, -5)



if __name__== "__main__":
    main(argv)

