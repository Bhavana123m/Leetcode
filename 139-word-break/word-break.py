class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def recurse(start, s, memo):
            if start == len(s):
                return True
            if memo[start] != -1:
                if (memo[start] == 0):
                    return False
                
                return True

            for i in range(start, len(s)):
                sub_s = s[start:i+1]
                if sub_s in wordDict and recurse(i+1, s, memo):
                    memo[start] = 1
                    return True
            
            memo[start] = 0
            return False

        memo = [-1]*len(s)
        return recurse(0, s, memo)


        # for c in s:
        #     sub_s+=c
        #     if sub_s in wordDict:
        #         sub_s = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # word_set = set(wordDict)  
        # dp = [False] * (len(s)+1)
        # dp[len(s)] = True
        # for i in range(len(s)-1, -1, -1):
        #     for word in word_set:
        #         if (i + len(word)) <= len(s) and s[i : i+len(word)] == word:
        #             dp[i] = dp [i+len(word)]
        #         if dp[i]:
        #             break
        # return dp[0]
