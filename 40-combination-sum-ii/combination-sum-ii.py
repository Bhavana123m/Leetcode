class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set()
        candidates.sort()
        def calculate_comb(start, result, path):
            total = sum(path)
            if total == target:
                result.add(tuple(path[:]))
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                calculate_comb(i + 1, result, path)
                path.pop()
        calculate_comb(0, result, [])
        return list(result)