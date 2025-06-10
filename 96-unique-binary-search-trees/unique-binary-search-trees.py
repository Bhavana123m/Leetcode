class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
        #recursion O[3^n] : bcz 3 operations each node : left, right, center
        if n <=1:
            return 1
        count = 0
        for i in range(1, n+1):
            count+= self.numTrees(i-1) * self.numTrees(n-i)
        return count
        