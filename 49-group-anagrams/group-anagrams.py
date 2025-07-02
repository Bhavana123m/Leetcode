class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_dict = {} 
        
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1

            key = ""
            for count in char_count:
                key += str(count) + "#" 
            if key in result_dict:
                result_dict[key].append(s)
            else:
                result_dict[key] = [s]

        return list(result_dict.values())
            
        
















































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