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

def batchGetCanonicalLabel(labels: list) -> list:
    process = './labelg'
    cmd = [process]
    for inputs in labels:
        cmd.append((inputs + '\n').encode('utf-8'))
        
    output = subprocess.check_output(cmd)
    print(output)

def getCanonicalLabel(label: str) -> str:
    cmd = ['./labelg']
    input = (label + '\n').encode('utf-8')
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, input=input)
    return result.stdout.decode('utf-8').strip('\n')

def _test():
    return

if __name__ == "__main__":
    '''Provide testing here.'''
    _test()