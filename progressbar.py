class progressbar:
    """a progress bar"""

    def __init__(self, segmentNum, maxValue, minValue=0, startValue=0):

        self.maxValue = maxValue
        self.minValue = minValue
        self.Value = startValue
        self.segmentNum = segmentNum

    def update(self, value):
        """print the progress bar with an updated value"""

        filledSegments = int(value
                             / (
                               (self.maxValue-self.minValue)
                                / self.segmentNum)
                             )
        print('\r['
              + '#'*filledSegments
              + '-'*(self.segmentNum-filledSegments) + ']',
              end='',
              flush=True)
