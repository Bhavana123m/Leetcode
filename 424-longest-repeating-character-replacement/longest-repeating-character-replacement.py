class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        start = 0
        max_freq = 0
        max_len = 0

        for end in range(len(s)):
            freq[s[end]] += 1
            max_freq = max(max_freq, freq[s[end]])

            # If the number of changes needed > k, shrink the window
            if (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len

        # start = 0
        # max_len = 0
        # while start<len(s):
        #     end = start
        #     remaining = k
        #     while end + 1 < len(s) and (s[end + 1] == s[start] or remaining > 0):
        #         if s[end + 1] != s[start]:
        #             remaining -= 1
        #         end += 1
        #     max_len = max(max_len, end - start + 1)
        #     start += 1
        # return max_len
        #     while end<len(s) and s[end] == s[end+1]:
        #         end+=1
        #     while end<len(s) and s[end]!=s[end+1] and additional>0:
        #         end+=1
        #         additional-=1
        #     max_len = max(max_len, end-start)
        #     if end<len(s) and start<=end and s[start]!=s[end] and additional<=0:
        #         while start<=end and s[start]==s[end]:
        #             start+=1
        # return max_len