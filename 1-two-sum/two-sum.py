class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (i!=j and nums[i] + nums[j] == target):
        #             return [i, j]
        # return []

        num_index_map = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in num_index_map:
                return [i, num_index_map[num]]
            num_index_map[nums[i]] = i
        return []


        