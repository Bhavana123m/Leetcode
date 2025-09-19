class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map_st = {}
        map_ts = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a in map_st and map_st[a] != b:
                return False
            if b in map_ts and map_ts[b] != a:
                return False
            map_st[a] = b
            map_ts[b] = a

        return True
        

        # Wrong approach
        # if len(s)!=len(t):
        #     return False
        # map1 = {}
        # map2 = {}
        # i = 0
        # while i<len(s):
        #     if s[i] not in map1:
        #         map1[s[i]]=1
        #     else:
        #         map1[s[i]]+=1
        #     if t[i] not in map2:
        #         map2[t[i]]=1
        #     else:
        #         map2[t[i]]+=1
        #     i+=1
        # values1 = map1.values()
        # values2 = map2.values()
        # values1.sort()
        # values2.sort()
        # if values1 == values2:
        #     return True
        # return False
