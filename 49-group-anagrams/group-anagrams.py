class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == [""] or len(strs)==1:
            return [strs]
        result_dict = defaultdict(list)
        for s in strs:
            alph_arr = [0]*26
            for c in s:
                alph_arr[ord(c) -ord('a')]+=1
            key = ""
            for i in range(0,26):
                key += str(alph_arr[i])
                key+='#'
            result_dict[key].append(s)
        result = []
        for key in result_dict:
            result.append(result_dict[key])
        return result
            
        
















































        if strs == [""] or len(strs) == 1:
            return [strs]
        map_word = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in map_word:
                map_word[sorted_str].append(s)
            else:
                map_word[sorted_str] = [s]
        return list(map_word.values())