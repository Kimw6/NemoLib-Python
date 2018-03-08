#!/usr/bin/python3

# The GraphParser class parses a text file into a Graph object. Each row of
# input text file represents an edge in the graph. Each row should consist of
# two integers separated by whitespace, with each integer representing a
# vertex. Vertices are created automatically based on the edge information.
# Self edges and unconnected vertices are not allowed.

from undirected_graph import UndirectedGraph
from random import shuffle
import sys

# """
# port argparse
# parser = 
# argparse.ArgumentParser(description='Create a graph object from a text file')
# parser.add_argument('--directed', 'd', help='for a directed graph')
# parser.add_argument('--undirected', 'u', help='for an undirected graph')
# parser.add_argument('')
# """

def parseUndirected(infile:str) -> UndirectedGraph:
    outGraph = UndirectedGraph()
    edgeHolder = {}
    # vertices = set()
    
    with open(infile, 'r') as f:
        for line in f:
            # print(line)
            thisEdge = line.split()
            # print(thisEdge)
            print(thisEdge, '.')
            if len(thisEdge) > 2:
                print('Too many vertices')
            elif len(thisEdge) > 0:
                if thisEdge[0] in edgeHolder.keys():
                    edgeHolder[thisEdge[0]].append(int(thisEdge[1]))
                else:
                    thisList = []
                    thisList[0] = int(thisEdge[1])
                    edgeHolder[int(thisEdge[0])] = thisList[0]
                # vertices.add(thisEdge[0])
                # vertices.add(thisEdge[1])

    print(edgeHolder)
    # for v in vertices:
    #     outGraph.
    for _ in edgeHolder.keys():
        outGraph.addVertex()

    for key, values in edgeHolder.items():
        for v in values:
            outGraph.addEdge(key, v)
    
    return outGraph

if __name__ == '__main__':
    ''' do some testing stuff like -
    call main function using filename 
    provided in command line call'''
    inf = ''
    if len(sys.argv) > 1:
        inf = sys.argv[1]
    else:
        inf = 'test4parse.txt'
    testGraph = UndirectedGraph()
    testGraph = parseUndirected(inf)
    print(testGraph)