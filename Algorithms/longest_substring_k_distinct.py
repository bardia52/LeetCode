class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}
        ans = 0
        low = 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                j = min(d.values())
                del d[s[j]]
                low = j + 1
            ans = max(ans, i-low+1)
        return ans