from . undirected_graph import UndirectedGraph

class Subgraph(UndirectedGraph):
    _subgraphSize = 0

    def __init__(self, size):
        super()
        self._subgraphSize = size

    def addVertex(self):
        if self._numNodes >= self._subgraphSize:
            print("The subgraph is full: Cannot add more")
            return -1

        return UndirectedGraph.addVertex(self)

    def contains(self, vertex):
        for v in self._adjacencyLists :
            if (v == vertex):
                return True
        return False

    def get(self, index):
        if (index > self.getSize()):
            print(index, "the index is not available")
            return -1
        return self._adjacencyLists[index]
