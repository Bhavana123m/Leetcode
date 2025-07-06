class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""

        # Step 1: Build the frequency map of characters in t
        t_count = {}
        for c in t:
            if c not in t_count:
                t_count[c] = 1
            else:
                t_count[c] += 1

        window = {}
        have = 0
        need = len(t_count)
        start = 0
        end = 0
        pointers = (-1, -1)
        min_len = float('inf')

        while end < len(s):
            c = s[end]
            if c not in window:
                window[c] = 0
            window[c] += 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                # Update the result
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    pointers = (start, end)

                # Shrink from the left
                left_char = s[start]
                window[left_char] -= 1
                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1
                start += 1

            end += 1

        if pointers == (-1, -1):
            return ""
        return s[pointers[0]:pointers[1]+1]









# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         if len(s)<len(t):
#             return ""
#         t_count = {}
#         for c in t:
#             if c not in t_count:
#                 t_count[c] = 1
#             else:
#                 t_count[c]+=1
#         start = 0
#         end = 0
#         min_len = float('inf')
#         pointers = (-1,-1)
        
#         def check_count(map):  #IF total count > 0 True-> then move end
#             counts = map.values()
#             if max(counts)>0:
#                 return True
#             return False
        
        
#         while end<len(s):
#             map = dict(t_count)
            
#             if check_count(map):  #If total_Count > 0 True and move end
#                 if s[end] in map:
#                     map[s[end]]-=1
#                 end+=1
           
#             while max(map.values()) == 0:
#                 min_len = min(min_len, end-start+1)
#                 pointers = (start, end)
#                 if s[start] in map:
#                     map[s[start]]+=1
#                 start+=1

#         return s[pointers[0]:pointers[1]+1]
                


