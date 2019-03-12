class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.array = [0]*size
        self.pointer = 0
        self.sizeMet = False
        self.ave = float(0)
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.array[self.pointer] = val
        self.pointer += 1
        if self.pointer == self.size:
            self.pointer = 0
            self.sizeMet = True
        if not self.sizeMet:
            self.ave = float(sum(self.array[0:self.pointer])) / float(self.pointer)
        else:
            self.ave = float(sum(self.array)) / float(self.size)
        return self.ave
