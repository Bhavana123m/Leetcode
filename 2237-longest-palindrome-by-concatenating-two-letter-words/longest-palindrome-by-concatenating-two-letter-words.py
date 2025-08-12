class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solutions/1675343/python3-java-c-counting-mirror-words-o-n
        m = defaultdict(int)
        length = 0
        unpaired = 0
        for w in words:
            if w[0] == w[1]:
                if m[w] > 0:
                    unpaired -=1
                    m[w]-=1
                    length+=4
                else:
                    m[w]+=1
                    unpaired+=1
            else:
                if m[w[::-1]]>0:
                    length+=4
                    m[w[::-1]]-=1
                else:
                    m[w]+=1
        if unpaired > 0:
            length+=2
        return length