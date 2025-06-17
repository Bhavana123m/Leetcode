class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        # if len(nums) != len(set(nums)):
        #     return True
        # else:
        #     return False
        # previous = set()
        # for i in nums:
        #     if i in previous:
        #         return True
        #     previous.add(i)
        # return False
        