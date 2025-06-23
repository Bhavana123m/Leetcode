class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        unique =[]
        for char in s:
            if not unique:
                unique.append(char)
            else:
                if unique[-1] == char:
                    unique.pop()
                else:
                    unique.append(char)
        return "".join(unique)
