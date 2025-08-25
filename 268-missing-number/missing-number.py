class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for num in nums:
            ans^=num
        for i in range(0, n+1):
            ans^=i
        return ans
        
        # n = len(nums)
        # actual_sum = sum(nums)
        # expected_sum = (n * (n+1))//2
        # return expected_sum - actual_sum
        