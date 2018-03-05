from undirected_graph import UndirectedGraph
import random


def generateGraph(sourceGraph: UndirectedGraph) -> UndirectedGraph:
    '''Generates a random graph of the same size and compexity of an input graph.'''
    dsv = getDegreeSequenceVector(sourceGraph)
    newGraph = UndirectedGraph()
    vertexList = []
    for i in range(0, sourceGraph.getSize()):
        newGraph.addVertex()
        for j in range(0, dsv[i]):
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


if __name__ == "__main__":
    '''Provide testing here.'''
    import random

    graph = UndirectedGraph()

    for i in range(0, 12):
        graph.addVertex()

    graph.addEdge(0, 3)
    graph.addEdge(0, 2)
    graph.addEdge(7, 8)
    graph.addEdge(1, 8)
    graph.addEdge(1, 2)
    graph.addEdge(1, 4)
    graph.addEdge(3, 2)
    graph.addEdge(7, 11)
    graph.addEdge(3, 9)
    graph.addEdge(3, 10)
    graph.addEdge(9, 11)
    graph.addEdge(9, 6)
    graph.addEdge(11, 6)
    graph.addEdge(11, 10)
    graph.addEdge(10, 4)
    graph.addEdge(5, 4)

    randomGraph = generateGraph(graph)

    print(graph)
    print(randomGraph)
