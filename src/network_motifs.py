import nemolib.graph.graph_parser as graph_parser
import nemolib.graph.graph_generator as graph_generator
import nemolib.esu.esu as esu
import nemolib.labels.labelg as labelg
import nemolib.statistics.justin_statistics as stats

if __name__ == "__main__":
    '''Provide testing here.'''
    graph = graph_parser.parseGraph('exampleGraph.txt')
    subgraphs = esu.getAllSubgraphs(graph, 4, [1, 1, 1, 1])
    random_graphs = graph_generator.generateGraphSet(graph, 10)
    random_subgraphs = []
    for r_graph in random_graphs:
        print('Enumerating...')
        random_subgraphs.append(esu.getAllSubgraphs(r_graph, 4, [.5, .5, .5, .5]))

    data_labels, random_labels = labelg.graphsToG6Labels(subgraphs, random_subgraphs)

    random_mean_frequency = stats.randomMeanFrequency(data_labels, random_labels)
    means = random_mean_frequency

    # Making all data relative frequencies
    data_labels = stats.relativeFrequency(data_labels)
    for index in range(0, len(random_labels)):
        random_labels[index] = stats.relativeFrequency(random_labels[index])

    relative_frequency = data_labels

    std = stats.standardDeviation(data_labels, random_labels, means)
    z = stats.zScore(data_labels, means, std)
    p = stats.pValue(z)

    all_labels = set()
    for label in data_labels:
        all_labels.add(label)

    for l in random_labels:
        for label in l:
            all_labels.add(label)

    # print(data_labels)

    print('Label \t RelFrequency \t RandMeanFreq \t Z-Score \t P-Value')
    for label in all_labels:
        if label not in relative_frequency:
            relative_frequency[label] = 0
        if label not in random_mean_frequency:
            random_mean_frequency[label] = 0

        print(label, '\t', '{0:.4f}'.format(relative_frequency[label] * 100), end=' \t ')
        print('{0:.4f}'.format(random_mean_frequency[label] * 100), '\t', '{0:.4f}'.format(z[label]), '\t', '{0:.4f}'.format(p[label]))
