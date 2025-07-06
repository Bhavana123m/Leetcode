class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def recurse(s, memo):
            if not s:
                return 1

            if s[0] == '0':
                memo[s] = 0
                return 0

            if s in memo:
                return memo[s]
            a = recurse(s[1:], memo)
            memo[s[1:]] = a
            if len(s)>1 and int(s[:2])<27:
                a = recurse(s[1:], memo)
                b = recurse(s[2:], memo)
                memo[s[1:]] = a
                memo[s[2:]] = b
                return a + b
            
            
            return a
            
        memo = {}
        return recurse(s, memo)
            # return recurse(s[start], s[start:start+2])




















































































        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 #one way to decode for 0
        dp[1] = 1 #one way to decode for 1
        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])
            if one_digit != 0:
                dp[i] += dp[i - 1]
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
