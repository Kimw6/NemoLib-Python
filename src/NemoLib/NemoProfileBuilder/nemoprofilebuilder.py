
#import java.util.Map


class NemoProfileBuilder:

    def __init__(self):
        raise AssertionError()

	@classmethod
    def build(cls, sp, sa, pThresh):
        result = SubgraphProfile()
        pValues = sa.getPValues()
        for labelPValue in pValues.entrySet():
            if labelPValue.getValue() <= pThresh:
                print labelPValue.getKey()
                result.addFrequencies(labelPValue.getKey(), sp.getFrequencies(labelPValue.getKey()))
        return result
