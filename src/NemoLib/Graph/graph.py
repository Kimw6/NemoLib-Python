# 
#  Implementation of graph data structure to manage network graphs.
#  
from NemoLib.Graph.adjacencylist import AdjacencyList

# Look into serialization
class Graph:

    #graph constructor
    def __init__(self):
        self._adjacencyLists = []
        self._maxNodeId = 0
    
#      #Add a vertex to this Graph.
#      #return the ID number assigned to the new vertex
    def addVertex(self):
        self._adjacencyLists.push(AdjacencyList())
        return self._adjacencyLists.__len__() - 1
        
#      Add an edge between two existing vertices on this graph.
#      @param vertexA One of the vertices between which to addSubgraph an edge.
#      @param vertexB The other vertex.
#      @return true if both vertexA and vertexB exist in this Graph; false
#      otherwise.     
    def addEdge(self, vertexA, vertexB):
        if (vertexA > self._adjacencyLists.__len__() - 1 
            or vertexB > self._adjacencyLists.__len__() - 1):
            
            return False
        else:
            self._adjacencyLists[vertexA].push(vertexB)
            self._adjacencyLists[vertexB].push(vertexA)
            return True
        
#   Get the getSize of this Graph
#   @return the getSize of this graph
    def getSize(self):
        return self._adjacencyLists.__len__()
    
#     get the adjacency list for a given node
    def getAdjacencyList(self, index):
        return self.adjacencyLists[index]

#    get index of a node given the node's name
#    create an entry if it does not exist     
#    @param String    nodeName name mapped to a vertex
#    @param Dict      nameToIndex  defines index of name
#    @returns Number  the index of a node with nodeName
    def getOrCreateIndex(self, nodeName, nameToIndex):
        if (nodeName not in nameToIndex):
            nameToIndex.put(nodeName, self.adjacencyLists.size())
            self.adjacencyLists.add(AdjacencyList())
        return nameToIndex.get(nodeName)

# 
#     /**
#      * Return a string representation of this Graph object.
#      * @return
#      */
#     @Override
#     public String toString() {
#         Set<Edge> edges = new HashSet<>();
#         for(int i = 0; i < adjacencyLists.size(); i++) {
#             AdjacencyList curAdjList = adjacencyLists.get(i);
#             CompactHashSet.Iter adjListItr = curAdjList.iterator();
#             while(adjListItr.hasNext()) {
#                 edges.add(new Edge(i, adjListItr.next()));
#             }
#         }
#         StringBuilder sb = new StringBuilder();
#         for(Edge edge : edges) {
#             sb.append(edge).append('\n');
#         }
#         return sb.toString();
#     }


# Represents edges for a Graph
class _Edge:
    
    def __init__(self, *args):
        self.nodeA = args[0]
        self.nodeB = args[1]
 
#       @Override
        def __eq__(self, other):
            if (type(other) is not type(self)):
                return False

            return ((self.nodeA == other.nodeA and
                    self.nodeB == other.nodeB) or
                    (self.nodeA == other.nodeB and
                    self.nodeB == other.nodeA))
            
        #       @Override
        def __neq__(self, other):
            return not self == other

#       @Override
        def __str__(self):
            return "[", str(self.nodeA) , ", ",  str(self.nodeB), "]"
