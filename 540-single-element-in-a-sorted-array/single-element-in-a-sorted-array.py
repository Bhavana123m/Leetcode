class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low + high)//2
            if mid == 0:
                if nums[mid] != nums[mid+1]:
                    return nums[mid]
            elif mid == len(nums)-1:
                if nums[mid-1] != nums[mid]:
                    return nums[mid]
            elif nums[mid] != nums[mid+1] and nums[mid-1] != nums[mid]:
                return nums[mid]
            if mid%2 == 0:
                if nums[mid-1] == nums[mid]:
                    high = mid-1
                elif nums[mid] == nums[mid+1]:
                    low = mid+1
            else:
                if nums[mid-1] == nums[mid]:
                    low = mid+1
                elif nums[mid] == nums[mid+1]:
                    high = mid-1
        return low