class AdjacencyList:
# 
#  AdjacencyList represents all adjacent vertices for a particular vertex in a
#  network graph.
#  
    def __init__(self, adjList):
        if (type(adjList) is set):
            self._nodes = set.copy(adjList)
        else:
            self._nodes = {}
            
    def add(self, node):
        self._nodes.add(node)
    
    def __iter__(self):
        return self.__iter__(self._nodes)
        
    def contains(self, node):
            return self._nodes.__contains__(node)

    def size(self):
        return self._nodes.__len__()
    
    def isEmpty(self):
        return self.__len__() is 0

    def __str__(self):
        return str(self._nodes)

    def remove(self, node):
        return self._nodes.remove(node)

    def copy(self):
        return AdjacencyList(self._nodes)
