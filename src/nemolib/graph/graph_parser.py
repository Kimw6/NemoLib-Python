#!/usr/bin/python3

# The GraphParser class parses a text file into a Graph object. Each row of
# input text file represents an edge in the graph. Each row should consist of
# two integers separated by whitespace, with each integer representing a
# vertex. Vertices are created automatically based on the edge information.
# Self edges and unconnected vertices are not allowed.

# GraphParser may be called from command line with one optional arg - filename

try:
    from .undirected_graph import UndirectedGraph
except Exception: #ImportError
    from undirected_graph import UndirectedGraph 
import sys
from random import shuffle

# parseGraph accepts a string as a parameter
# infile is the filepath to a text file containing
#   two nodes per line to represent each edge of the graph
# Function will parse the file, building a set of unique vertices
#   and an associative array containing each primary vertex as a key
#   and each vertex they connect with as a list of ints for the value
# Unsure of how much validation/error checking is necessary here
#
def parseGraph(infile:str) -> UndirectedGraph:
    outGraph = UndirectedGraph()
    edgeHolder = {}
    vertices = set()
    lines = []

    # in case of empty string parameter
    if not infile:
        print('Error: no file given')
        outGraph.addVertexByName(0)
        return outGraph

    with open(infile, 'r') as f:
        for line in f:
            thisEdge = line.split()
            lines.append(thisEdge)

    # probably a wasted step
    shuffle(lines)

    for l in lines:
        if l:
            intA = int(l[0])
            intB = int(l[1])
            vertices.add(intA)
            vertices.add(intB)
            # print(thisEdge, '.')
            if intA in edgeHolder.keys():
                edgeHolder[intA].append(intB)
            else:
                edgeHolder[intA] = [intB]

    #print(edgeHolder)

    for vertex in vertices:
        outGraph.addVertexByName(vertex)

    for key, values in edgeHolder.items():
        for v in values:
            outGraph.addEdge(outGraph.getVertexByName(key), outGraph.getVertexByName(v))

    return outGraph

if __name__ == '__main__':
    # do some testing stuff like
    # call main function using filename
    # provided in command line call
    inf = ''
    if len(sys.argv) > 1:
        inf = sys.argv[1]
    else:
        inf = 'test4parse.txt'

    testGraph = UndirectedGraph()
    testGraph = parseGraph(fpath)
    print(testGraph)