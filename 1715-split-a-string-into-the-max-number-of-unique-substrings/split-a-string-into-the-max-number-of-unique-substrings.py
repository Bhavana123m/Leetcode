class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        substrings = []
        def get_substr(index, substrings, path):
            if index == len(s):
                if len(path) > len(substrings):
                    substrings[:] = path[:]
                return
            if len(path) + (len(s) - index) <= len(substrings):
                return
            for i in range(index + 1, len(s) + 1):
                piece = s[index:i]
                if piece in path:
                    continue
                path.append(piece)
                get_substr(i, substrings, path)
                path.pop()
        get_substr(0, substrings, [])
        return len(substrings)