class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subsets = []
        def get_subsets(index, subsets, path):
            add = path[:]
            if add not in subsets:
                subsets.append(add)
            for i in range(index, len(nums)):
                path.append(nums[i])
                get_subsets(i+1, subsets, path)
                path.pop()            
        get_subsets(0, subsets, [])
        return subsets