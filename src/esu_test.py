from nemolib.esu import ryan_esu
from nemolib.graph import undirected_graph
from nemolib.labels import labelg

import sys

if __name__ == "__main__":
    '''Provide testing here.'''
    if len(sys.argv) > 1:
        graph_size = int(sys.argv[1])
        probability = float(sys.argv[2])
    else:
        graph_size = 5
        probability = 1.0

    testGraph = undirected_graph.getSimpleTestGraph()

    # Use nemolib-java-style probability list
    probabilityList = []
    for _ in range(0, graph_size - 1):
        probabilityList.append(1)

    probabilityList.append(probability)

    subgraphs = ryan_esu.getAllSubgraphs(testGraph, graph_size, probabilityList)

    result = labelg.getG6LabelCount(subgraphs)

    for label in result:
        print(label, ':', result[label])
