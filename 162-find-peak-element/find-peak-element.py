class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak = nums[0]
        peak_idx = 0
        nums.append(-float('inf'))
        start = 1
        # end = len(nums)
        while start<len(nums)-1:
            if nums[start-1]<nums[start]>nums[start+1]:
                if peak<nums[start]:
                    peak_idx = start
                peak = max(peak, nums[start])
            start+=1
        # print(peak)
        return peak_idx