from .. graph.subgraph import Subgraph
import subprocess


def getG6Label(graph: Subgraph) -> str:
    adjacencyMatrix = { }

    for i in range(0, graph.getSize()):
        adjacencyMatrix[i] = { }
        for j in range(0, graph.getSize()):
            adjacencyList = graph.getAdjacencyList(i)
            if j in adjacencyList:
                adjacencyMatrix[i][j] = True
            else:
                adjacencyMatrix[i][j] = False

    binary = ''
    for i in adjacencyMatrix:
        for j in adjacencyMatrix[i]:
            if i > j:
                if adjacencyMatrix[i][j]:
                    binary += '1'
                else:
                    binary += '0'

    while len(binary) % 6 != 0:
        binary += '0'

    chars = []
    num_segments = int(len(binary) / 6)
    for i in range(0, num_segments):
        chars.append(binary[i * 6 : i * 6 + 6])

    rx = ''
    for char in chars:
        binary = int(char, 2)
        binary += 63
        binary = bin(binary)
        binary = binary[2:]
        #binary = binary[len(binary) - 6:]
        rx += chr(int(binary, 2))

    nn = chr(63 + graph.getSize())
    return nn + rx

def getG6LabelCount(graphs: list) -> dict:

    result = { }
    for graph in graphs:
        label = getG6Label(graph)
        label = getCanonicalLabel(label)
        if label in result:
            result[label] += 1
        else:
            result[label] = 1

    return result

def batchGetCanonicalLabel(labels: list, knownLabels: dict) -> dict:
    f = open("input.txt","w+")
    input = []

    # add labels without known canonical labels to input.txt
    for inputs in labels:
        if (inputs not in knownLabels):
            f.write(inputs+ '\n')
            input.append(inputs)
    f.close()
    # run labelg for the unknown labels
    cmd = ['./labelg', 'input.txt', 'output.txt']
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
    
    # add newly found labels: canonical label key values pairs to knownLabels
    f = open("output.txt", "r")
    index = 0
    for lines in f:
        knownLabels[input[index]] = lines.strip()
        index += 1
    f.close()

    return knownLabels

def getCanonicalLabel(label: str) -> str:
    cmd = ['./labelg']
    input = (label).encode('utf-8')
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, input=input)
    return result.stdout.decode('utf-8').strip('\n')

def _test():
    labels = batchGetCanonicalLabel(['DqC','DpG','DpC','DiG','DiC','DhC','DxG','DxC'], {})
    for l in labels:
        print(l,": ", labels[l])


if __name__ == "__main__":
    '''Provide testing here.'''
    _test()