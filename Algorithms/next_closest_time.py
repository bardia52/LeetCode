class Solution(object):

    # Assuming nums is a list with single digit int with length of 4
    def timeCreator(self, nums):
        times = []
        for hour1 in nums:
            for hour2 in nums:
                hour = hour1*10 + hour2
                if (hour>=0) and (hour<24):
                    for min1 in nums:
                        for min2 in nums:
                            min = min1*10+min2
                            if (min<60):
                                times.append(str(hour)+":"+str(min))
        #print times
        return times

    def numExtractor(self, time):
        nums=[int(time[0]), int(time[1]), int(time[3]), int(time[4])]
        return nums

    diffCalculator(self, time1, time2):
        

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = self.numExtractor(time)
        print nums
        self.timeCreator(nums)
