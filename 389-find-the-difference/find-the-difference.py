class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        arr = [0]*26
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
            arr[ord(t[i])-ord('a')]-=1
        for i in range(26):
            if arr[i] !=0:
                return chr(i+ord('a'))
