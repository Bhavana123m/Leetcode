class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # char_arr = [0]*26
        # for c in s:
        #     char_arr[ord(c)-ord('a')]+=1
        # max_freq = max(char_arr)
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c]+=1
        max_freq = max(freq.values())
        if max_freq>(n+1)//2:
            return ""
        reorganised_string = [None]*n
        idx = 0
        # for i in range(n):
        for char, count in sorted(freq.items(), key=lambda x: -x[1]):
            for _ in range(count):
                if idx>=n:
                    idx = 1
                reorganised_string[idx] = char
                idx+=2
        return "".join(reorganised_string)

