class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLen = min(len(s),k)
        for m in range(len(s)):
            # start of string is s[m]
            for n in range(m+1,len(s)+1):
                tempLen = len(''.join(set(s[m:n])))
                if tempLen > k:
                    break
                elif n-m > maxLen:
                    maxLen = n-m
        return maxLen
