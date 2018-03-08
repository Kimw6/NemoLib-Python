
'''
 * The GraphParser class parses a text file into a Graph object. Each row of
 * input text file represents an edge in the graph. Each row should consist of
 * two integers separated by whitespace, with each integer representing a
 * vertex. Vertices are created automatically based on the edge information.
 * Self edges and unconnected vertices are not allowed.
'''
#!/usr/bin/env python
from nemolib.graph import undirected_graph
from random import shuffle
import sys

'''
import argparse
parser = 
argparse.ArgumentParser(description='Create a graph object from a text file')

parser.add_argument('--directed', 'd', help='for a directed graph')
parser.add_argument('--undirected', 'u', help='for an undirected graph')
parser.add_argument('')'''

def parseUndirected(infile: str) -> UndirectedGraph:
    outGraph = UndirectedGraph()
    edgeHolder = {}
    # vertices = set()
    
    with open('infile', 'r') as f:
        for line in f:
            thisVertices = line.split()
            if len(thisVertices) > 2:
                print('Too many vertices')
            try:
                edgeHolder[thisVertices[0]].append(thisVertices[1])
            except KeyError:
                edgeHolder[thisVertices[0]] = thisVertices[1]
            # vertices.add(thisVertices[0])
            # vertices.add(thisVertices[1])

    # for v in vertices:
    #     outGraph.
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
        inf = './test4parse.txt'
    testGraph = UndirectedGraph()
    testGraph = parseUndirected(inf)
    print(testGraph)