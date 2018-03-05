from NemoLib.Graph import undirected_graph


class Subgraph(undirected_graph):
    
    _subgraphSize = 0


    def __init__(self, size):
        super(self)
        self._subgraphSize = size
    
    def copy(self):
        copy = Subgraph(self._order)
        for vertex in self._nodes :
            copy.add(vertex)
        return copy
            
    def addVertex(self):
        if(self.isComplete()):
            print("The subgraph is full:: Cannot add more")
            return
   
        super.addVertex()

    def addEdge(self, vertexA, vertexB):
        '''Add an edge between two vertices. Both vertices must exist. Return true if the edge was added; false otherwise.'''
        if vertexA > self._numNodes - 1 or vertexB > self._numNodes - 1:
            return False
        elif(self.isComplete() is False):
            print("subgraph is full")
            return False
        else:
            self._adjacencyLists[vertexA].add(vertexB)
            self._adjacencyLists[vertexB].add(vertexA)
            return True
    
    def isComplete(self):
        return len(self._nodes) == self._subgraphSize
            
    
    def getSubgraphSize(self):
        return self._subgraphSize
    

    def contains(self, vertex):
        for v in self._nodes :
            if (v == vertex):
                return True
        return False

    def get(self, index):
        if (index > self.getSize()):
            print(index, "th index is not available")
            return -1
        return self._nodes[index]
