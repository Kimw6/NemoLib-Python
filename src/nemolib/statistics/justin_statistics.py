import random
import math

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
    ''' Calculate the relative frequencies for each subgraph in the original graph'''
    n = 0
    for values in dataSet:
        n+= dataSet[values]
    frequencies = {}
    for values in dataSet:
        frequencies[values] = dataSet[values]/n
    return frequencies

def randomMeanFrequency(dataSet: dict,sampleData: list) -> dict:
    ''' Calculate the relative frequencies for subgraphs using all of the subgraphs'''
    freqsToCalc = {}
    sum = 0
    for values in dataSet:
        freqsToCalc[values] = 0
    for samples in sampleData:
        for sampleValues in samples:
            sum+=samples[sampleValues]
            if sampleValues in freqsToCalc:
                freqsToCalc[sampleValues] += samples[sampleValues]
    for values in freqsToCalc:
        freqsToCalc[values] = freqsToCalc[values]/sum
    return freqsToCalc
       
def mean(originalData: dict, sampleData: list) -> dict:
    ''' Calculate the mean frequency for each subgraph '''
    count = 0
    sums = {}
    for values in originalData:
        if not values in sums:
            sums[values] = originalData[values]
        else:
            sums[values] += originalData[values]
    count+=1

    for samples in sampleData:
        count+=1
        for sampleValues in samples:
            if sampleValues in sums:
                sums[sampleValues] += samples[sampleValues]
     
    results = {}
    for values in sums:
        results[values] = sums[values]/count  
    
    return results;

def standardDeviation(originalData: dict,  sampleData: list, means: dict) -> dict:
    ''' Calculate the standard deviation for each subgraph in the original graph'''
    std = {}
    diffFromMeanSq = {}
    n = 1
    for values in originalData:
        diffFromMeanSq[values] = math.pow(originalData[values] - means[values],2)
    for samples in sampleData:
        n +=1
        for sampleValues in samples:
            if sampleValues in originalData:
                diffFromMeanSq[sampleValues] += math.pow(samples[sampleValues] - means[values],2)
    for values in diffFromMeanSq:
        if (n <= 1):
            print("invalid sample size")
            return {}
        std[values] = math.sqrt(diffFromMeanSq[values]/(n-1))         
    
    return std

def zScore(originalData: dict, means: dict, standardDeviations: dict) -> dict:
    ''' calculate the Z score for each subgraph in the original graph'''
    z = {}
    for values in originalData:
        z[values] = (originalData[values] - means[values])/standardDeviations[values]
    
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