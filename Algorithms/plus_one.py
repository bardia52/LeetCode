class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for d in digits:
            num *= 10
            num += d
        num += 1
        array = []
        while num > 0:
            d = num % 10
            num //= 10
            array.insert(0,d)
        return array