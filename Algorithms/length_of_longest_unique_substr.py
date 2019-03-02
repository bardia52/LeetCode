class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = start = maxLen = 0
        usedChars = {}
        for i in range(len(s)):
            if s[i] in usedChars and start <= usedChars[s[i]]:
                start = usedChars[s[i]]+1
            else:
                maxLen = max(maxLen, i-start+1)
            usedChars[s[i]] = i
        return maxLen
