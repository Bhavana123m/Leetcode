class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n == 0:
            return [""]
        
        output = []
        result = []

        def recurse(i):
            if len(output) == n:
                result.append(''.join(output))
                return
            ch = s[i]
            if ch.isalpha():
                output.append(ch.lower())
                recurse(i + 1)
                output.pop()

                output.append(ch.upper())
                recurse(i + 1)
                output.pop()
            else:
                output.append(ch)
                recurse(i + 1)
                output.pop()

        recurse(0)
        return result
