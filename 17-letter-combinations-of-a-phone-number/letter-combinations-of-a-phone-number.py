class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        hash_num_letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
        '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        list_alp = []
        for d in digits:
            list_alp.append(hash_num_letters[d])
        result = ['']
        for letters in list_alp:
            temp = []
            for prefix in result:
                for letter in letters:
                    temp.append(prefix + letter)
            result = temp
        # from itertools import product
        # result = [''.join(pair) for pair in product(*list_alp)]
        return result