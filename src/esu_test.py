from NemoLib.esu import ryan_esu
from NemoLib.graph import undirected_graph

import sys

if __name__ == "__main__":
    '''Provide testing here.'''
    if len(sys.argv) > 1:
        graph_size = int(sys.argv[1])
    else:
        graph_size = 3

    testGraph = undirected_graph.getSimpleTestGraph()

    subgraphs = ryan_esu.getAllSubgraphs(testGraph, graph_size)

    for graph in subgraphs:
        print(graph)
