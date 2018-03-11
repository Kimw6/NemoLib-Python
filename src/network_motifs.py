import nemolib.graph.graph_parser as graph_parser
import nemolib.graph.graph_generator as graph_generator
import nemolib.esu.esu as esu
import nemolib.labels.labelg as labelg
import nemolib.statistics.justin_statistics as stats
from timeit import default_timer as timer

if __name__ == "__main__":
    '''Provide testing here.'''
    start = timer()
    graph = graph_parser.parseGraph('exampleGraph.txt')
    subgraphs = esu.getAllSubgraphs(graph, 4, [1, 1, 1, 1])
    random_graphs = graph_generator.generateGraphSet(graph, 100)
    random_subgraphs = []
    for r_graph in random_graphs:
        print('Enumerating...')
        random_subgraphs.append(esu.getAllSubgraphs(r_graph, 4, [.5, .5, .5, .5]))

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
