class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count+=1
            else:
                max_count = max(count, max_count)
                count = 0
        return max(count, max_count)

        # max_count = 0
        # count = 0
        # n = len(nums)
        # for start in range(n):
        #     if nums[start] == 1:
        #         start+=1
        #         count+=1
        #     else:
        #         max_count = max(max_count, count)
        #         count = 0
        #         while start< n and nums[start] == 0:
        #             start+=1
        # max_count = max(max_count, count)
        # return max_count
