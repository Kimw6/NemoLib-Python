# from NemoLib.Subgraph.subgraphenumerationresult import SubgraphEnumerationResult
# from NemoLib.Graph.graph import Graph
# from NemoLib.Subgraph.subgraph import Subgraph
# import math
# import random
# class RandESU:

#     self.probs = {}

# #
# #private RandESU()
# #{
# #    throw new AssertionError();
# #}
# 	def __init__(self):
#         raise AssertionError()

#     def __init__(self, probs):
#         self.probs = probs


# #   Enumerates all subgraphSize Subgraphs in the input Graph using the
# #   RAND-ESU algorithm.
# #   @param graph           the graph on which to execute RAND-ESU
# #   @param subgraphSize    the getSize of the target Subgraphs

#     def enumerate(graph, subgraphSize, subgraphs):
#         selectedVertices = {}
#         if (probs.get(0) == 1.0):
#             for i in graph.getSize(graph):
#                 selectedVertices.append(i)
#         else:
#             numVerticesToSelect = math.round(probs[0] * graph.getSize(graph))
#             for i in numVerticesToSelect:
#                 nodeSelected = random.randint(0, graph.getSize(graph))
#                 while(if nodeSelected in selectedVertices):
#                     nodeSelected = random.randint(0, graph.getSize(graph))
#                 selectedVertices.append(nodeSelected)
#         for vertex in selectedVertices:
#             enumerate(self, graph, subgraphs, subgraphSize, probs, vertex)
                    
# #   Enumerates all subgraphSize Subgraphs for the specified vertex's branch
# #   of an ESU execution tree using the RAND-ESU algorithm. Allows for more
# #   control over execution order compared to the enumerate method that does
# #   not include a vertex parameter.
# #   @param graph the graph on which to execute RAND-ESU
# #   @param subgraphs
# #   @param subgraphSize
# #   @param probs
# #   @param vertex
#     def enumerate(self, graph, subgraphs, subgraphSize, probs, vertex):
#         subgraph = Subgraph(subgraphSize)
#         adjacenyList = {}
# 		iter = graph.getAdjacencyList(vertex).iterator()
# 		while(iter.hasNext()):
# 			if next > vertex:
# 				adjacencyList.add(next)
# 		subgraph.add(vertex, graph.getAdjacencyList(vertex))
# 		if self._shouldExtend(probs.get(1)):
# 			extend(self, graph, subgraph, adjacencyList, probs, subgraphs)
			
# 	def extend(self, graph, subgraph, extension, probs, subgraphs):
# 		v = subgraph.root()
# 		wIter = extension.iterator()
		
# 		if len(subgraph) == subgraph.order() - 1:
# 			while wIter.hasNext():
# 				if self._shouldExtend(probs.get(len(probs) - 1)):
# 					subgraphUnion = subgraph.copy()
# 					subgraphUnion.add(self, w, graph.getAdjacencyList(w))
# 					#synchronized(subgraphs)
# 					with subgraphs:
# 						subgraphs.addSubgraph(subgraphUnion)
		
		
# 		while wIter.hasNext():
# 			wIter.remove()
# 			nextExtension = extension.copy()
# 			uIter = graph.getAdjacencyList(w).iterator()
# 			while uIter.hasNext():
# 				u = uIter.next()
# 				if u > v:
# 					if self._isExclusive(self, graph, u, subgraph):
# 						nextExtension.add(u)
# 			subgraphUnion = subgraph.copy()
# 			subgraphUnion.add(self, w, graph.getAdjacencyList(w))
			
# 			if self._shouldExtend(probs.get(len(subgraphUnion) - 1)):
# 				self.extend(self, graph, subgraphUnion, nextExtension, probs, subgraphs)
		
# #	Determines whether or not to extend based on given probability, given as an interger.
# #	Precondition 0.0 <= prob <= 1.0

# 	def _shouldExtend(self, prob):
# 		if prob == 1.0:
# 			return True
# 		if prob == 0.0:
# 			return False
# 		if prob > 1.0 or prob < 0.0:
# 			raise IllegalArgumentException("RAND-ESU probability outside" + " acceptable range (0.0 to 1.0)")
# 		randomNum = random.randint(0, 99) + 1
# 		return randomNum <= prob * 100.0
		
# #	Returns true if the node index is exclusive to the given subgraph
# #	(that is, is not already in the subgraph, and is not adjacent to any of the nodes in the subgraph)

# 	def _isExclusive(self, graph, node, subgraph):
# 	i = 0
# 	while i < len(subgraph):
# 		subgraphNode = subgraph.get(i)
# 		if subgraphNode == node:
# 			return False
# 		i += 1
		
# 	i = 0
# 	while i < len(subgraph):
# 		subgraphNode = subgraph.get(i)
# 		if graph.getAdjacencyList(subgraphNode).contains(node):
# 			return False
# 		i += 1
    
# 	return True
