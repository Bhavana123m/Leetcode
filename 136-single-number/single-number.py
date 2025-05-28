class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result = i^result
        return result
        # return 2 * sum(set(nums)) - sum(nums)