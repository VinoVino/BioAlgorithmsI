__author__ = 'jcovino'
from sys import argv
"""
ODE CHALLENGE: Solve the Change Problem. The DPCHANGE pseudocode is reproduced below for your convenience.
     Input: An integer money and an array Coins = (coin1, ..., coind).
     Output: The minimum number of coins with denominations Coins that changes money.

Sample Input:
     40
     50,25,20,10,5,1

Sample Output:
     2
solution from: http://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html
"""

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin


def main(argv):

    amnt = 16096
    clist = [14,7,5,3,1]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    #print("They are:")
    #printCoins(coinsUsed,amnt)
    #print("The used list is as follows:")
    #print(coinsUsed)



if __name__== "__main__":
    main(argv)