class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = [1,2,3,4,5,6,7,8,9]
        def calculate_comb(start, result, path):
            total = sum(path)
            if total == n and len(path) == k:
                result.append(path[:])
            if total > n:
                return
            for i in range(start, 10):
                path.append(i)
                calculate_comb(i+1, result, path)
                path.pop()
        calculate_comb(1, result, [])
        return result