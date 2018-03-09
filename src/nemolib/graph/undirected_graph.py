class UndirectedGraph:
    '''Implementation of graph data structure to manage network graphs.'''

    _adjacencyLists = []
    _nodesByName = {}
    _numNodes = 0

    def __init__(self):
        '''Constructor creates an empty graph.'''
        self._adjacencyLists = []
        self._maxNodeID = 0

    def addVertex(self):
        '''Add a vertex to the graph. The vertex is added with no edges. Return the ID assigned to the vertex.'''
        self._adjacencyLists.append(set())
        self._numNodes += 1
        return self._numNodes - 1

    def addVertexByName(self, nodeName):
        if (nodeName in self._nodesByName):
            return -1
        else:
            index = self.addVertex()
            self._nodesByName[nodeName] = index
            return index

    def addEdge(self, vertexA: int, vertexB: int):
        '''Add an edge between two vertices. Both vertices must exist. Return true if the edge was added; false otherwise.'''
        if vertexA > self._numNodes - 1 or vertexB > self._numNodes - 1:
            return False
        else:
            self._adjacencyLists[vertexA].add(vertexB)
            self._adjacencyLists[vertexB].add(vertexA)
            return True

    def getSize(self):
        '''Return the number of nodes in the graph.'''
        return self._numNodes

    def getAdjacencyList(self, index: int):
        '''Return the adjacency list for a particular node.'''
        return self._adjacencyLists[index]

    def getVertexByName(self, nodeName: str):
        '''Get the index of a node given its name. Create the node if it doesn't exist.'''
        if (nodeName not in self._nodesByName):
            return self.addVertexByName(nodeName)
        else:
            return self._nodesByName[nodeName]

    def __str__(self):
        '''Get a string representation of this graph.'''
        edges = set()
        for i, adjacencyList in enumerate(self._adjacencyLists):
            for vertex in adjacencyList:
                edges.add(_UndirectedEdge(i, vertex))

        string = ''
        for edge in edges:
            string += edge.__str__()
            string += '\n'

        return string


class _UndirectedEdge:
    '''Represents a single edge for an UndirectedGraph.'''
    _nodeA = -1
    _nodeB = -1

    def __init__(self, nodeA: int, nodeB: int):
        if nodeA < nodeB:
            self._nodeA = nodeA
            self._nodeB = nodeB
        else:
            self._nodeA = nodeB
            self._nodeB = nodeA

    def __eq__(self, other):
        '''Return true if the two nodes match the other's two nodes (in either order).'''
        if (type(other) is not type(self)):
            return False

        return ((self._nodeA == other._nodeA and self._nodeB == other._nodeB) or
                (self._nodeA == other._nodeB and self._nodeB == other._nodeA))

    def __neq__(self, other):
        '''Return false if the two edges are not the same.'''
        return not self == other

    def __str__(self):
        '''Return a string representation of this edge.'''
        return '[' + str(self._nodeA) + ', ' + str(self._nodeB) + ']'

    def __hash__(self):
        return hash((self._nodeA, self._nodeB))

def getSimpleTestGraph():
    graph = UndirectedGraph()

    for _ in range(0, 12):
        graph.addVertex()

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(1, 4)
    graph.addEdge(1, 8)
    graph.addEdge(2, 3)
    graph.addEdge(3, 9)
    graph.addEdge(3, 10)
    graph.addEdge(4, 5)
    graph.addEdge(6, 9)
    graph.addEdge(6, 11)
    graph.addEdge(7, 8)
    graph.addEdge(7, 11)
    graph.addEdge(9, 11)
    graph.addEdge(10, 11)

    return graph

if __name__ == "__main__":
    '''Provide testing here.'''
    import random

    graph = UndirectedGraph()

    for i in range(0, 25):
        graph.addVertex()

    for i in range(0, 25):
        graph.addEdge(random.randint(0, 24), random.randint(0, 24))

    print(graph.__str__())
