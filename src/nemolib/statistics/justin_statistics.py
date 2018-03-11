import random
import math
from copy import deepcopy

'''Class that handle required statistical calculation for sets of data stored in dicts'''

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
    ''' Calculate the relative frequencies for each subgraph in the original graph'''
    n = 0
    for values in dataSet:
        n+= dataSet[values]
    frequencies = {}
    for values in dataSet:
        frequencies[values] = dataSet[values]/n
    return frequencies

def makeDatasetRelative(dataSet: list) -> list:
    index = 0
    for sets in dataSet:
        sum = 0
        for keys in sets:
            sum += sets[keys]
        for keys in sets:
            dataSet[index][keys] = dataSet[index][keys]/sum
        index += 1
    return dataSet

# sampleData should be relative frequencies
def randomMeanFrequency(dataSet: dict, sampleData: list) -> dict:

    frequencySums = {}
    meanFreqs = {}
    for keys in dataSet:
        frequencySums[keys] = 0;
        meanFreqs[keys] = 0;

    for samples in sampleData:
        for keys in samples:
            if keys in dataSet:
                frequencySums[keys] += samples[keys]

    for keys in meanFreqs:
        meanFreqs[keys] = frequencySums[keys]/len(sampleData)

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

    for values in originalData:
        diffFromMeanSq[values] = 0
    for samples in sampleData:
        for sampleValues in samples:
            if sampleValues in originalData:
                diffFromMeanSq[sampleValues] += math.pow(samples[sampleValues] - means[sampleValues],2)
    for values in diffFromMeanSq:
        std[values] = math.sqrt(diffFromMeanSq[values]/(len(sampleData)-1))
    return std

def zScore(originalData: dict, means: dict, standardDeviations: dict) -> dict:
    ''' calculate the Z score for each subgraph in the original graph'''
    z = {}
    for values in originalData:
        try:
            z[values] = (originalData[values] - means[values])/(standardDeviations[values])
        except:
            z[values] = (originalData[values] - means[values])/.000001

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
    originalData = {'C~': 64, 'CR': 42694, 'C^': 372, 'CF': 78113, 'Cr': 1009, 'CN': 5232}
    
    relOriginalData = relativeFrequency(originalData)
    print(relOriginalData)
    print()
    
    comparisonData = []
    comparisonData.append({'CR': 1988, 'CF': 2309, 'CN': 61, 'Cr': 3})
    comparisonData.append({'CR': 2556, 'C^': 1, 'CN': 64, 'CF': 2487, 'Cr': 1})
    comparisonData.append({'CR': 2109, 'CF': 1670, 'CN': 10, 'Cr': 3})
    comparisonData.append({'CR': 2009, 'C^': 1, 'CN': 26, 'CF': 2488, 'Cr': 7})
    comparisonData.append({'CN': 178, 'Cr': 3, 'CF': 3484, 'C^': 5, 'CR': 2987})
    

    makeDatasetRelative(comparisonData)

    for x in comparisonData:
        print (x)
        
    print()
    means = randomMeanFrequency(relOriginalData, comparisonData)
    print(means)
    
    std = standardDeviation(relOriginalData, comparisonData, means)
    print(std)
    z =zScore(relOriginalData,means,std)
    print(z)
    p = pValue(z)
    print(p)

if __name__ == "__main__":
    _test()