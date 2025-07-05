class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -float('inf')
        start = 0
        total = 0
        result = ()
        for i in range(len(nums)):
            total+=nums[i]
            if total > ans:
                ans = total
                result = (start, i)
            if total<0:
                total = 0
                start = i + 1
        return ans
                
