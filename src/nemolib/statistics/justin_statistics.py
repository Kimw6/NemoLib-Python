import random
import statistics as s

def generateTestData(size : int):
    dataset = {}
    for x in range(size):
        value = random.randint(1,size)
        if not value in dataset:
            dataset[value] = 1
        else:
            dataset[value] += 1
            
    return dataset

def mean(originalData: dict, sampleData: list) -> dict:
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
            if not sampleValues in sums:
                sums[sampleValues] = samples[sampleValues]
            else:
                sums[sampleValues] += samples[sampleValues]
     
    results = {}
    for values in sums:
        results[values] = sums[values]/count  
    
    return results;

def _test():
    originalData = generateTestData(10)
    comparisonData = []
    for x in range(99):
        comparisonData.append(generateTestData(10))

    
    mean(originalData, comparisonData)
    
if __name__ == "__main__":
    _test()