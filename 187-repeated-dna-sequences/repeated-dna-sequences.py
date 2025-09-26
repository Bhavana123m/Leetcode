class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n<=10:
            return []
        seq = set() 
        res = []     
        i = 0
        j = 0
        while j <= n:
            j = i + 9
            pattern = s[i:j+1]
            if pattern in seq and pattern not in res:
                res.append(pattern)
            else:
                seq.add(pattern)
            i+=1
            j+=1
        return res

        