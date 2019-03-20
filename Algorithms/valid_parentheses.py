class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            l = len(stack)
            if ch == ')':
                if l == 0 or stack.pop() != '(':
                    return False
            elif ch == '}':
                if l == 0 or stack.pop() != '{':
                    return False
            elif ch == ']':
                if l == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(ch)
        if len(stack) == 0:
            return True
        else:
            return False