class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        subsets = []

        self.backtrack(0, subsets, [])
        return subsets
    
    def backtrack(self, index, subsets, curr):
        subsets.append(curr[:])

        for i in range(index, len(self.nums)):

            curr.append(self.nums[i])
            self.backtrack(i + 1, subsets, curr)
            curr.pop()