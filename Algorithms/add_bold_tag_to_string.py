class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        arr = [False] * len(s)
        for d in dict:
            inx = l = 0
            while True:
                temp = s[inx:]
                inx1 = s[inx:].find(d)
                l = len(d)
                if inx1 != -1:
                    arr[inx1+inx:inx1+inx+l] = [True]*l
                    inx += inx1+1
                else:
                    break
        bias = 0
        if arr[0]:
            s = '<b>' + s
            bias += 3
        for ax in range(1,len(arr)):
            if arr[ax] and not arr[ax-1]:
                s = s[0:bias+ax] + '<b>' + s[bias+ax:]
                bias += 3
            if not arr[ax] and arr[ax-1]:
                s = s[0:bias+ax] + '</b>' + s[bias+ax:]
                bias += 4
        if arr[len(arr)-1]:
            s = s + '</b>'
        return s