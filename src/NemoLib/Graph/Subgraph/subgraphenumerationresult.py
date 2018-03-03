

class SubgraphEnumerationResult:


#   Adds a Subgraph to this SubgraphEnumerationResult
#   @param currentSubgraph a Subgraph to addSubgraph to this
#   SubgraphEnumerationResult
    def addSubgraph(self, currentSubGraph):

#   Merges g6 labels into SubgraphProfile labels. Recommended to use the
#   Labeler class to accomplish this.
    def label(self):

#   Calculates and returns a map of relative frequencies or concentrations
#   of labels in this subgraph.
#   @return The map of relative frequencies

    def getRelativeFrequencies(self):

