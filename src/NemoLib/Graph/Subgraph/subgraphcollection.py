

#import java.util.HashSet
#import java.util.Set

class SubgraphCollection:
    subGraphs = Set()

    @overloaded
    def __init__(self):
        raise AssertionError()

    @__init__.register(object, int)
    def __init___0(self, subgraphSize):
        self.subgraphs = HashSet()

    def add(self, subgraph):
        self.subgraphs.add(subgraph)
