class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        visited = set()
        start = 0
        end = 0
        max_len = -float('inf')
        while end<len(s):
            while s[end] in visited:
                visited.remove(s[start])
                start+=1
            visited.add(s[end])
            max_len = max(max_len, end-start+1)
            end+=1

        return max_len

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        length = 0
        start = 0
        visited = set()
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[start])
                start+=1
            visited.add(s[i])
            length = max(length, i-start+1)
        return length

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        start = 0
        end = 0
        max_len = 0
        seen = set()

        while end < len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
            max_len = max(max_len, end - start + 1)
            end+=1
        return max_len









        start = 0
        end = 0
        max_len = 0
        map_num_cnt={}
        while start<len(s):
            if s[start] in map_num_cnt:
                end = max(end, map_num_cnt[s[start]]+1)
            max_len = max(max_len, start-end+1)
            map_num_cnt[s[start]] = start
            start+=1
        return max_len
        # for i in range(0, len(s)):
        #     if s[i] in map_num_cnt.keys():
        #         max_len = max(max_len, len(map_num_cnt.keys()))
        #         ind = map_num_cnt[s[i]]
        #         print(ind)
        #         print(s[i])
        #         map_num_cnt[s[i]] = i
        #     else:
        #         map_num_cnt[s[i]] = i
        # print(map_num_cnt)

