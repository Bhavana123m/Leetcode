class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        outer = [[]]
        for num in nums:
            n = len(outer)
            for i in range(n):
                internal = outer[i] + [num]
                outer.append(internal)
        return outer