import nemolib.graph.graph_parser as graph_parser
import nemolib.graph.graph_generator as graph_generator
import nemolib.esu.esu as esu
import nemolib.labels.labelg as labelg
import nemolib.statistics.justin_statistics as stats
from timeit import default_timer as timer

import sys
import multiprocessing
from multiprocessing import Pool
import os

sourceGraph = None
subgraph_size = 3
sample_enumeration_probabilities = [.5, .5, .5]

def f(num_random_graphs) -> list:
    random_subgraphs = []
    random_graphs = graph_generator.generateGraphSet(graph, num_random_graphs)
    for r_graph in random_graphs:
        print(os.getpid(), 'Enumerating...')
        random_subgraphs.append(esu.getAllSubgraphs(r_graph, subgraph_size, sample_enumeration_probabilities))

    return random_subgraphs

if __name__ == "__main__":
    '''Provide testing here.'''
    if len(sys.argv) != 4:
        print("Usage: python network_motifs.py <graph> <subgraph_size> <num_random_graphs>")

    try:
        filepath = sys.argv[1]
        subgraph_size = int(sys.argv[2])
        num_random_graphs = int(sys.argv[3])
    except:
        print("An error occurred.")
        sys.exit()

    full_enumeration_probabilities = []
    for _ in range(0, subgraph_size):
        full_enumeration_probabilities.append(1)

    sample_enumeration_probabilities = []
    for _ in range(0, subgraph_size):
        sample_enumeration_probabilities.append(0.5)

    start = timer()

    graph = graph_parser.parseGraph(filepath)
    subgraphs = esu.getAllSubgraphs(graph, subgraph_size, full_enumeration_probabilities)

    use_multiprocessing = True

    random_subgraphs = []

    if use_multiprocessing:
        num_cores = multiprocessing.cpu_count()

        task_distribution = []
        if num_random_graphs % num_cores == 0:
            for _ in range(0, num_cores):
                task_distribution.append(num_random_graphs // num_cores)
        else:
            for _ in range(0, num_cores - 1):
                task_distribution.append(num_random_graphs // num_cores)
            task_distribution.append(num_random_graphs % num_cores + (num_random_graphs // num_cores))

        p = Pool(num_cores)
        results = []
        sourceGraph = graph
        results = p.map(f, task_distribution)

        for r in results:
            random_subgraphs += r
    else:
        random_graphs = graph_generator.generateGraphSet(graph, num_random_graphs)
        for r_graph in random_graphs:
            print('Enumerating...')
            random_subgraphs.append(esu.getAllSubgraphs(r_graph, subgraph_size, sample_enumeration_probabilities))

    data_labels, random_labels = labelg.graphsToG6Labels(subgraphs, random_subgraphs)

    relative_data_labels = stats.relativeFrequency(data_labels)
    stats.makeDatasetRelative(random_labels)
    means = stats.randomMeanFrequency(relative_data_labels , random_labels)


    std = stats.standardDeviation(relative_data_labels, random_labels, means)
    z = stats.zScore(relative_data_labels, means, std)
    p = stats.pValue(z)

    all_labels = set()
    for label in data_labels:
        all_labels.add(label)

    # print(data_labels)

    print('Label \t RelFrequency \t RandMeanFreq \t Z-Score \t P-Value')
    for label in all_labels:
        if label not in relative_data_labels:
            relative_data_labels[label] = 0
        if label not in means:
            means[label] = 0

        print(label, '\t', '{0:.4f}'.format(relative_data_labels[label] * 100), '%', end=' \t ')
        print('{0:.4f}'.format(means[label] * 100), '%',  '\t', '{0:.4f}'.format(z[label]), '\t', '{0:.4f}'.format(p[label]))

    end = timer()

    print("execution time: ", end - start)
