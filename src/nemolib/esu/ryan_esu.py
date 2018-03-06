from .. graph.undirected_graph import UndirectedGraph
from .. graph.undirected_graph import getSimpleTestGraph
from .. graph.graph_generator import generateGraph

import random

def nodesToGraph(graph: UndirectedGraph, nodeList: list) -> UndirectedGraph:
    '''Take a list of Vertex IDs for a given graph and return them as a Graph object.'''
    mapping = { }
    subgraph = UndirectedGraph()

    for n in nodeList:
        mapping[n] = subgraph.addVertex()

    for n in nodeList:
        adjacencyList = graph.getAdjacencyList(n)
        for a in adjacencyList:
            if a in nodeList and mapping[a] < subgraph.getSize():
                subgraph.addEdge(mapping[n], mapping[a])

    return subgraph

def getAllSubgraphs(graph: UndirectedGraph, graphSize: int, probabilityList: list) -> list:
    '''Enumerate through ESU algorithm and retrieve all subgraphs of a given size for this graph.'''
    subgraphList = list()
    exclusionList = []
    for i in range(0, graph.getSize()):
        nodeList = [i]
        neighborList = []
        for n in graph.getAdjacencyList(i):
            if n not in exclusionList and n not in nodeList and n not in neighborList:
                neighborList.append(n)

        getSubgraphs(graph, graphSize, nodeList, neighborList, exclusionList, subgraphList, probabilityList)
        exclusionList.append(i)

    subgraphs = list()
    for g in subgraphList:
        subgraphs.append(nodesToGraph(graph, g))

    return subgraphs

def getSubgraphs(graph: UndirectedGraph, remainingLayers: int, nodeList: list,
                 neighborList: list, exclusionList: list, subgraphList: list,
                 probabilityList: list):
    '''Recursive call to find all subgraphs for a given graph and size.'''
    chance = random.uniform(0, 1)
    if chance > probabilityList[0]:
        return

    if remainingLayers == 1:
        subgraphList.append(nodeList)
        return

    newExclusionList = list(exclusionList)

    for node in neighborList:
        newNodeList = nodeList + [node]

        newNeighborList = list(neighborList)
        newNeighborList.remove(node)
        for n in newExclusionList:
            if n in newNeighborList:
                newNeighborList.remove(n)

        for n in graph.getAdjacencyList(node):
            if n not in newExclusionList and n not in newNodeList and n not in newNeighborList:
                newNeighborList.append(n)

        newExclusionList.append(node)
        getSubgraphs(graph, remainingLayers - 1, newNodeList, newNeighborList, newExclusionList, subgraphList, probabilityList[1:])

    return





def _test():
    graph = getSimpleTestGraph()

    subgraphs = getAllSubgraphs(graph, 3, .5)

    for g in subgraphs:
        print(g)

if __name__ == "__main__":
    '''Provide testing here.'''
    _test()
