from NemoLib.Subgraph.subgraphenumerationresult import SubgraphEnumerationResult
from NemoLib.Graph.graph import Graph

class ESU:


    def __init__(self):


#   Enumerates Subgraphs using the ESU algorithm. Requires user to specify
#   return type(s) and provide the accompanying data structures.
#   @param graph the graph on which to execute ESU
#   @param subgraphs the SubgraphEnumerationResult into which to enumerated
#   Subgraphs will be stored.
#   @param subgraphSize the getSize of the target Subgraphs
    def enumerate(self, graph, subgraphSize, subgraphs):
        for i in graph.getSize(graph):
            enumerate(self, graph, subgraphs, subgraphSize, i)
        
#   Enumerates Subgraphs for one branch of the ESU tree starting at the
#   given node. Allows for more control over the order the order of 
#   execution, but does not perform a full enumeration.
#
#   @param graph the graph on which to execute ESU
#   @param subgraphs the data structure to which results are written
#   @param subgraphSize the target subgraph getSize to enumerate
#   @param vertex the graph vertex at which to execute
    def enumerate(self, graph, subgraphs, subgraphSize, vertex):
        self.probs = {}
        for i in subgraphSize:
            probs.append(1.0)
        RandESU.enumerate(graph, subgraphs, subgraphSize, probs, vertex)
