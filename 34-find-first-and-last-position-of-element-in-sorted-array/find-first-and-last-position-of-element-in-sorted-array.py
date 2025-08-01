class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1,-1]
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] == target:
                result[0]=mid
                high = mid-1
            elif nums[mid]>target:
                high= mid-1
            else:
                low = mid+1
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] == target:
                result[1]=mid
                low = mid+1
            elif nums[mid]>target:
                high= mid-1
            else:
                low = mid+1
        if result[0] == -1 or result[1] == -1 or result[0] > result[1]:
            return [-1, -1]
        return result