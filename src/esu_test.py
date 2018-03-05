from nemolib.esu import ryan_esu
from nemolib.graph import undirected_graph
from nemolib.labels import labelg

import sys

if __name__ == "__main__":
    '''Provide testing here.'''
    if len(sys.argv) > 1:
        graph_size = int(sys.argv[1])
    else:
        graph_size = 5

    testGraph = undirected_graph.getSimpleTestGraph()

    subgraphs = ryan_esu.getAllSubgraphs(testGraph, graph_size)

    result = labelg.getG6LabelCount(subgraphs)

    for label in result:
        print(label, ':', result[label])
