class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLen = min(len(s),k)
        for m in range(len(s)):
            setDistinct = {s[m]}
            # start of string is s[m]
            for n in range(m+1,len(s)):
                if (s[n] not in setDistinct):
                    setDistinct.add(s[n])
                numDistinct = len(setDistinct)
                if numDistinct > k:
                    break
                strLen = n-m+1
                if (strLen > maxLen):
                    maxLen = strLen
        return maxLen
