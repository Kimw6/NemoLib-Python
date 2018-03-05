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

#     def __init__(self, probs):
#         self.probs = probs


# #   Enumerates all subgraphSize Subgraphs in the input Graph using the
# #   RAND-ESU algorithm.
# #   @param graph           the graph on which to execute RAND-ESU
# #   @param subgraphSize    the getSize of the target Subgraphs

#     def enumerate(graph, subgraphSize, subgraphs):
#         selectedVertices = {}
#         if probs[0] == 1.0:
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

