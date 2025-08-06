class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0 or n==1:
            return s
        stack = []

        for i in s:
            if stack and i!=stack[-1] and(i.lower() == stack[-1] or i.upper() == stack[-1]):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)



        n = len(s)
        if n == 0 or n==1:
            return s
        stack = []
        i = 0
        while i<n:
            while i<n and stack:
                top = stack[-1]
                if top.islower():
                    if top.upper() == s[i]:
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    if top.lower() == s[i]:
                        stack.pop()
                    else:
                        stack.append(s[i])
                i+=1
            if i<n:
                stack.append(s[i])
            i+=1
        return "".join(stack)

        