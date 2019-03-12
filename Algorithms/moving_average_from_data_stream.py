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
        oldVal = self.array[self.pointer]
        self.array[self.pointer] = val
        if not self.sizeMet:
            self.ave = float(sum(self.array[0:self.pointer+1])) / float(self.pointer+1)
        else:
            self.ave += (float(val-oldVal) / float(self.size))
        self.pointer += 1
        if self.pointer == self.size:
            self.pointer = 0
            self.sizeMet = True
        return self.ave

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
