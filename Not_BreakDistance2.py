__author__ = 'jcovino'
__author__ = 'jcovino'
from sys import argv
from collections import defaultdict


"""
CODE CHALLENGE: Solve the 2-Break Distance Problem.
     Input: Genomes P and Q.
     Output: The 2-break distance d(P, Q).

Sample Input:
     (+1 +2 +3 +4 +5 +6)
     (+1 -3 -6 -5)(+2 -4)

Sample Output:
     3
"""

''

def two_break_dist(P, Q):
    '''Returns the 2-Break Distance of Circular Chromosomes P and Q.'''

    # Construct the break point graph of P and Q.
    graph = defaultdict(list)
    for perm_cycle in P+Q:
        L = len(perm_cycle)
        for i in xrange(len(perm_cycle)):
            # Add the edge between consecutive items (both orders since the breakpoint graph is undirected).
            # Note: Modulo L in the higher index for the edge between the last and first elements.
            graph[perm_cycle[i]].append(-1*perm_cycle[(i+1) % L])
            graph[-1*perm_cycle[(i+1) % L]].append(perm_cycle[i])

    # BFS to find the number of connected components in the breakpoint graph.
    component_count = 0
    remaining = set(graph.keys())
    while len(remaining) > 0:
        component_count += 1
        queue = [remaining.pop()]  # Components are cyclic, so starting point is unimportant.
        while queue:
            current = queue.pop(0)
            queue += filter(lambda node: node in remaining, graph.get(current, []))
            remaining -= set(queue)  # Overkill, but it's nice and concise!

    # Theorem: d(P,Q) = blocks(P,Q) - cycles(P,Q)
    print"blocks----", sum(map(len,P))
    print "P+Q", component_count
    return sum(map(len,P)) - component_count




def main(argv):
    with open(argv[1],"r") as fstream:
        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in fstream.readlines()]
        P = [map(int, block.split()) for block in P]
        Q = [map(int, block.split()) for block in Q]


    #print P
    #print Q

        # Get the 2-Break Distance.
    dist = two_break_dist(P, Q)

    sumTotal=0
    for element in P:
        sumTotal=len(element)+sumTotal
    print sumTotal

    # Print and save the answer.
    print str(dist)
        

if __name__== "__main__":
    main(argv)
