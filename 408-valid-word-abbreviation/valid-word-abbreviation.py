class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0
        s = word
        n, m = len(s), len(abbr)
        last_token_was_number = False

        while i < n and j < m:
            if abbr[j].isspace():
                j += 1
            elif abbr[j].isalpha():
                if s[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                last_token_was_number = False
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                if last_token_was_number:
                    return False

                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
                if i > n:
                    return False
                last_token_was_number = True
            else:
                return False

        return i == n and j == m