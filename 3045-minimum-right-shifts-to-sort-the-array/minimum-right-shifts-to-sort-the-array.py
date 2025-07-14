class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        c = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                idx = i
                c+=1
            if c>1:
                return -1
        if idx == 0:
            return 0
        
        if nums[len(nums)-1]>nums[0]:
            return -1
        
        return len(nums)-idx