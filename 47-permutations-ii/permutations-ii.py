class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = set()
        used = [False]*len(nums)
        def get_perms(permutations, path):
            if len(nums) == len(path):
                permutations.add(tuple(path[:]))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                get_perms(permutations, path)
                path.pop()
                used[i] = False
        get_perms(permutations, [])
        return list(permutations)