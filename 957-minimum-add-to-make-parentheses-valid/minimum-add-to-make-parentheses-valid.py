class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        unattended_open_brackets = 0
        unattended_close_brackets = 0
        for t in s:
            if t == '(':
                unattended_open_brackets+=1
            elif t == ')':
                if unattended_open_brackets == 0:
                    unattended_close_brackets+=1
                else:
                    unattended_open_brackets-=1
        return unattended_close_brackets + unattended_open_brackets
