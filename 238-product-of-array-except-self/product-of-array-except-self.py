class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        count_zeroes = 0
        for num in nums:
            if num ==0:
                count_zeroes +=1
                continue
            product*=num
        for i in range(len(nums)):
            if count_zeroes == 0:
                nums[i] = product//nums[i]
            elif count_zeroes == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] =0
            else:
                nums[i] = 0
        return nums


