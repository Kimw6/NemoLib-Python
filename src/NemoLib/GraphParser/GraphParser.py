#!/usr/bin/env python
from sys import argv
from random import shuffle
import Graph

'''
 * The GraphParser class parses a text file into a Graph object. Each row of
 * input text file represents an edge in the graph. Each row should consist of
 * two integers separated by a single space, with each integer representing a
 * vertex. Vertices are created automatically based on the edge information.
 * Self edges and unconnected vertices are not allowed.
'''

'''
need to determine where files will be located
also determine functionality of this module,
should it also be able to produce graph files if used
as a standalone program?
'''

def main():
    nameToIndex = {}
    edges = []
    with open(infile, 'r') as f:
        for line in f:
            edges.apend(line)
    shuffle(edges)

    output = Graph.Graph()
    for edge in edges:
        temp            = edge.split()
        int fromIndex   = output.getOrCreateIndex(temp[0], nameToIndex)
        int toIndex     = output.getOrCreateIndex(temp[1], nameToIndex)

        if fromIndex != toIndex:
            output.getAdjacencyList(fromIndex.append(toIndex))
            output.getAdjacencyList(toIndex.append(fromIndex))

    return output


if __name__ == '__main__':
    main()