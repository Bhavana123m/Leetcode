class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        
        def extract_palindrome(string, left, right):
            count = 0
            while left >= 0 and right< len(s) and s[left] == s[right]:
                left-=1
                right+=1
                count+=1
            return count
        
        for i in range(len(s)):
            count += extract_palindrome(s, i, i)
            count += extract_palindrome(s, i, i+1)
        return count
            