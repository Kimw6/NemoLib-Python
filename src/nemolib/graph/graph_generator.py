from . undirected_graph import UndirectedGraph
from . undirected_graph import getSimpleTestGraph

import random
import multiprocessing
import os

def generateGraphSet(sourceGraph: UndirectedGraph, numGraphs: int, useMultiprocessing: bool = False) -> list:
    '''Create a set of random graphs based on the source graph.'''

    if useMultiprocessing:
        graphCount = []
        numCores = multiprocessing.cpu_count()

        if numGraphs % numCores == 0:
            for _ in range(0, numCores):
                graphCount.append(numGraphs // numCores)
        else:
            remainder = numGraphs % (numCores - 1)
            for _ in range(0, numCores - 1):
                graphCount.append(numGraphs // (numCores - 1))

            graphCount.append(remainder)

        graphLists = []
        for _ in graphCount:
            graphLists.append(list())

        processes = []

        for i, count in enumerate(graphCount):
            p = multiprocessing.Process(target=getGeneratedGraph, args=(sourceGraph, count, graphLists[i]))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        result = []
        for graphList in graphLists:
            result += graphList
    else:
        result = []
        for _ in range(0, numGraphs):
            result.append(generateGraph)

    return result

def getGeneratedGraph(sourceGraph: UndirectedGraph, count: int, graphs: list):
    '''Get a single generated graph and put it in a multiprocessing Queue.'''
    for _ in range(0, count):
        graphs.append(generateGraph(sourceGraph))

def generateGraph(sourceGraph: UndirectedGraph) -> UndirectedGraph:
    '''Generates a random graph of the same size and compexity of an input graph.'''
    dsv = getDegreeSequenceVector(sourceGraph)
    newGraph = UndirectedGraph()
    vertexList = []
    for i in range(0, sourceGraph.getSize()):
        newGraph.addVertex()
        for _ in range(0, dsv[i]):
            vertexList.append(i)

    random.shuffle(vertexList)

    while (True):
        u = random.randint(0, len(vertexList) - 1)

        # make sure v != u
        while True:
            v = random.randint(0, len(vertexList) - 1)
            if v != u:
                break

        # python-style swap
        if u > v:
            u, v = v, u

        edgeVertV = vertexList[v]
        edgeVertU = vertexList[u]

        del vertexList[v]
        del vertexList[u]

        newGraph.addEdge(edgeVertV, edgeVertU)
        if len(vertexList) <= 1:
            break

    return newGraph

def getDegreeSequenceVector(graph: UndirectedGraph) -> list:
    '''Generates a degree sequence vector from a graph.

    Each entry in the vector represents a vertex and the value represents
    the number of edges connected to that vertex.'''

    degreeSequenceVector = []
    for i in range(0, graph.getSize()):
        degree = len(graph.getAdjacencyList(i))
        degreeSequenceVector.append(degree)

    return degreeSequenceVector

def _test():
    import time

    graph = getSimpleTestGraph()

    start = time.time()
    generateGraphSet(graph, 100000, True)
    end = time.time()
    print(end - start)

    start = time.time()
    generateGraphSet(graph, 100000)
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    '''Provide testing here.'''
    _test()
