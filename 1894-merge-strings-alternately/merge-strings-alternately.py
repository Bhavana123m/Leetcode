class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            ans += word1[i]
            ans += word2[i]
        if len(word1) > len(word2):
            ans += word1[min_len:]
        else:
            ans += word2[min_len:]
        return ans
        
        result = ""
        left = 0
        size1 = len(word1)
        size2 = len(word2)
        remaining1 = 0
        remaining2 = 0 
        if size1>size2:
            size = size2
            remaining1 = size1-size2
        elif size1<size2:
            size = size1
            remaining2 = size2 - size1
        else:
            size = size1
        while left<size:
            result+=word1[left]
            result+=word2[left]
            left+=1
        while remaining1 > 0:
            result+=word1[left]
            remaining1-=1
            left+=1
        while remaining2 > 0:
            result+=word2[left]
            remaining2-=1
            left+=1
        return result

