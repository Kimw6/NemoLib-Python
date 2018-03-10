from .. graph.subgraph import Subgraph
import subprocess
import os

def graphsToG6Labels(graph: list, random_graphs: list):
    '''Takes in a list of graphs represented as a list of subgraphs and creates a list of labels.'''
    batch = set()
    label_count = {}
    for subgraph in graph:
        label = getG6Label(subgraph)
        if label in label_count:
            label_count[label] += 1
        else:
            label_count[label] = 1

        if label not in batch:
            batch.add(label)

    random_label_counts = []
    for random_graph in random_graphs:
        temp = {}
        for subgraph in random_graph:
            label = getG6Label(subgraph)
            if label in temp:
                temp[label] += 1
            else:
                temp[label] = 1

            if label not in batch:
                batch.add(label)

        random_label_counts.append(temp)

    canonical_map = batchGetCanonicalLabel(batch)

    canonical_label_count = {}
    for label in label_count:
        if canonical_map[label] not in canonical_label_count:
            canonical_label_count[canonical_map[label]] = 0
        canonical_label_count[canonical_map[label]] += label_count[label]

    canonical_random_label_counts = []
    for label_list in random_label_counts:
        temp = {}
        for label in label_list:
            if canonical_map[label] not in temp:
                temp[canonical_map[label]] = 0
            temp[canonical_map[label]] += label_list[label]
        canonical_random_label_counts.append(temp)

    return canonical_label_count, canonical_random_label_counts




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

def batchGetCanonicalLabel(labels: list, knownLabels: dict = {}) -> dict:
    #print(os.path.dirname(__file__) + '/../../../resources/')
    f = open('input.txt', 'w+')
    input = []

    # add labels without known canonical labels to input.txt
    for inputs in labels:
        if (inputs not in knownLabels):
            f.write(inputs+ '\n')
            input.append(inputs)
    f.close()
    # run labelg for the unknown labels
    cmd = [os.path.dirname(__file__) + '/../../../resources/labelg', 'input.txt', 'output.txt']
    p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    p.wait()

    # add newly found labels: canonical label key values pairs to knownLabels
    f = open('output.txt', 'r')
    index = 0
    for lines in f:
        knownLabels[input[index]] = lines.strip()
        index += 1
    f.close()

    os.remove('input.txt')
    os.remove('output.txt')

    return knownLabels

def getCanonicalLabel(label: str) -> str:
    cmd = [os.path.dirname(__file__) + '/../../../resources/labelg']
    input = (label + '\n').encode('utf-8')
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, input=input)
    return result.stdout.decode('utf-8').strip('\n')

def _test():
    labels = batchGetCanonicalLabel(['DqC','DpG','DpC','DiG','DiC','DhC','DxG','DxC'], {})
    for l in labels:
        print(l,": ", labels[l])


if __name__ == "__main__":
    '''Provide testing here.'''
    _test()
