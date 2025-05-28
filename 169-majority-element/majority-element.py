class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # map_rep = {}
        # for i in nums:
        #     # count = 1
        #     if map_rep and i in map_rep.keys():
        #         map_rep[i]+=1
        #     else:
        #         map_rep[i] = 1
        # for key in map_rep.keys():
        #     if map_rep[key] > n // 2:
        #         return key
        count = 0
        candidate = 0
        for i in range(len(nums)):
            if count == 0 and candidate!=nums[i]:
                candidate = nums[i]
                count+=1
            elif candidate==nums[i]:
                count+=1
            else:
                count-=1
        return candidate