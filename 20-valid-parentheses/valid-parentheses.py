

class Solution(object):
    def isValid(self, str):
        """
        :type s: str
        :rtype: bool
        """
        s = []
        for char in str:
            if char in '[{(':
                s.append(char)
            else:
                if len(s) == 0:
                    return False
                else:
                    if char == ')':
                        if s[-1] == '(':
                            s.pop()
                        else:
                            return False
                    elif char == '}':
                        if s[-1] == '{':
                            s.pop()
                        else:
                            return False
                    elif char == ']':
                        if s[-1] == '[':
                            s.pop()
                        else:
                            return False
        return not s
        