class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                if i != non_zero:
                    nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero+=1