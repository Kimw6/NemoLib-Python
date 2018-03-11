import random
import math
from copy import deepcopy

'''Class that handlew required statistical calculation for sets of data stored in dicts'''

def generateTestData(size: int):
    '''Generates tests data using integers'''
    dataset = {}
    for x in range(size):
        value = random.randint(1,size)
        if not value in dataset:
            dataset[value] = 1
        else:
            dataset[value] += 1
    return dataset

def relativeFrequency(dataSet: dict) -> dict:
    ''' Calculate the relative frequencies for each subgraph in a graph'''
    n = 0
    for values in dataSet:
        n+= dataSet[values]
    frequencies = {}
    for values in dataSet:
        frequencies[values] = dataSet[values]/n
    return frequencies

def randomMeanFrequency(dataSet: dict, sampleData: list) -> dict:
    ''' Calculate the relative frequencies for subgraphs using all of the subgraphs'''
    relFreqs = deepcopy(sampleData)
    meanFreqs = {}
    for keys in dataSet:
        meanFreqs[keys] = 0;

    for samples in relFreqs:
        for keys in samples:
            if keys in dataSet:
                meanFreqs[keys] += samples[keys]

    for keys in meanFreqs:
        meanFreqs[keys] = meanFreqs[keys]/len(sampleData)

    return meanFreqs

def mean(originalData: dict, sampleData: list) -> dict:
    ''' Calculate the mean frequency for each subgraph '''
    count = 0
    sums = {}
    for values in originalData:
            sums[values] = 0

    for samples in sampleData:
        count+=1
        for sampleValues in samples:
            if sampleValues in sums:
                sums[sampleValues] += samples[sampleValues]

    results = {}
    for values in sums:
        results[values] = sums[values]/count

    return results

def standardDeviation(originalData: dict,  sampleData: list, means: dict) -> dict:
    ''' Calculate the standard deviation for each subgraph in the original graph'''
    std = {}
    diffFromMeanSq = {}
    relativeValues = []
    for i in range(0, len(sampleData)):
        relativeValues.append(normalizeData(sampleData[i]))

    n = 0
    for values in originalData:
        diffFromMeanSq[values] = 0
    for samples in relativeValues:
        n += 1
        for sampleValues in samples:
            if sampleValues in originalData:
                diffFromMeanSq[sampleValues] += math.pow(samples[sampleValues] - means[sampleValues],2)
    for values in diffFromMeanSq:
        std[values] = math.sqrt(diffFromMeanSq[values]/(n-1))
    return std

def zScore(originalData: dict, means: dict, standardDeviations: dict) -> dict:
    ''' calculate the Z score for each subgraph in the original graph'''
    z = {}
    x = relativeFrequency(originalData)
    for values in x:
        z[values] = (x[values] - means[values])/(standardDeviations[values]+.000000001)

    return z

def _cdf(z:float):
    ''' cumaltive density function used for calculating p values '''
    return 0.5 * (1 + math.erf(z/math.sqrt(2)))

def pValue(zValues: dict) -> dict:
    ''' Calculate the P value, using a 2-tail test, for each subgraph in the original graph using Z values'''
    p = {}
    for values in zValues:
        #subtracting 1 from cdf value and multiplying result by 2 to get 2-tailed p value
        p[values] = 2*(1 - (_cdf(math.fabs(zValues[values]))))
    return p

def _test():
    originalData = generateTestData(10)
    comparisonData = []
    for x in range(100):
        comparisonData.append(generateTestData(10))



    means = mean(originalData, comparisonData)
    print(means)
    std = standardDeviation(originalData, comparisonData, means)
    #print(relativeFrequency(originalData))
    #print(randomMeanFrequency(originalData, comparisonData))
    print(std)
    z =zScore(originalData,means,std)
    print(z)
    p = pValue(z)
    print(p)

if __name__ == "__main__":
    _test()