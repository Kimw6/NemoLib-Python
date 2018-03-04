
from NemoLib.Subgraph.subgraphenumerator import SubgraphEnumerator

#  Analyzes a target graph to determine relative frequency of subgraph patterns.
class TargetGraphAnalyzer:

#    subgraphEnumerator = SubgraphEnumerator()
#    subgraphEnumerationResult = SubgraphEnumerationResult()
    

#   Default contructor for TargetGraphAnalyzer objects.
#   @param subgraphEnumerator the algorithm to be used to enumerate subgraphs for a target graph
#   @param subgraphEnumerationResule the data structure to use when storing
    def __init__(self, subgraphEnumerator, subgraphEnumerationResult):
        self.subgraphEnumerator = subgraphEnumerator
        self.subgraphEnumerationResult = subgraphEnumerationResult


#   Analyze the target graph to enumerate all subgraphSize subgraphs and
#   deposit the results into ths TargetGraphAnalyzer's subgraphEnumerator.
#   @param graph the graph to analyze
#   @param subgraphSize the size of the subgraphs to enumerate
#   @return a mapping of subgraph labels to their respective relative
#   frequencies in the target graph.
    def analyze(self, graph, subgraphSize):
        self.subgraphEnumerator.enumerate(graph, subgraphSize, self.subgraphEnumerationResult)
        self.subgraphEnumerationResult.label()
        return self.subgraphEnumerationResult.getRelativeFrequencies()


    
