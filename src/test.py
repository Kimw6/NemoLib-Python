import nemolib.labels.labelg as labelg

if __name__ == '__main__':
    labels = {}
    labels = labelg.batchGetCanonicalLabel(['Bw', 'BW', 'Bw'], labels)
    print(labels)
