class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False
        arr = [0]*26
        key1 = ""
        key2 = ""
        for c in word1:
            arr[ord(c)-ord('a')] += 1
        non_zero_indices_dict1 = {}
        for i in range(26):
            if arr[i]!=0:
               non_zero_indices_dict1[i] = arr[i] 
        arr = [0]*26
        for c in word2:
            arr[ord(c)-ord('a')] += 1
        non_zero_indices_dict2 = {}
        for i in range(26):
            if arr[i]!=0:
               non_zero_indices_dict2[i] = arr[i] 
        keys1 = non_zero_indices_dict1.keys()
        keys2 = non_zero_indices_dict2.keys()
        if keys1!= keys2:
            return False
        values1 = sorted(non_zero_indices_dict1.values())
        values2 = sorted(non_zero_indices_dict2.values())
        if values1 == values2:
            return True
        return False
