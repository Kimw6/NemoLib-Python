class Labeler():

    def __init__(self, subgraph):
        _subgraph = subgraph
    

class AdjacencyMatrix():
    
    _aMatrix = []
    _size = 0
    def __init__(self, size):
        self._size = size
        self._aMatrix =[[0 for x in range(size)] for y in range(size)] 
        print(self._aMatrix)
                

a = AdjacencyMatrix(1)