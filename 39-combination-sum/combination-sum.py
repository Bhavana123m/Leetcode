class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def calculate_comb(start, result, path):
            total = sum(path)
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                calculate_comb(i, result, path)
                path.pop()
        calculate_comb(0, result, [])

        return result