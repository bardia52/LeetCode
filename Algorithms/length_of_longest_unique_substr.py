class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isUnique(str):
            d = {}
            for m in str:
                if m in d:
                    return False
                else:
                    d[m] = 1
            return True
        maxLen = 0
        for m in range(len(s)):
            for n in range(m+1,len(s)+1):
                if isUnique(s[m:n]) and n-m > maxLen:
                    maxLen = n-m
        return maxLen
