class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return []
        res = []
        # the idea is to iteratively divide the last number in the factor combo into smaller numbers
        # [12] ---divide 12 by 2---> [2, 6]  ---divide 6 by 2---> [2, 2, 3] ---3 cannot divide 2 so done---
        # [12] ---divide 12 by 3---> [3, 4] (---divide 4 by 2---> [3, 2, 2])*
        # to fix the issue of duplicates (* above) we pass the starting number for the factor search
        #  so if you've divided by 2, next try dividing by 2 or higher (hence 2, 2, 3)
        #  but if you now divide by 3, start the next division at 3
        # why stop when i*i=num? because any number K>sqrt(num) will have num/K<K which is duplicative

        def dfs(curr, i):
            num = curr.pop()
            while i*i <= num:
                div = num/i
                if num%i == 0:
                    res.append(curr + [i, div])
                    dfs(curr + [i, div], i)
                i+=1
        
        dfs([n], 2)
        return res
