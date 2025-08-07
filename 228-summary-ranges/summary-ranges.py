class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == i:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start]) + "->" + str(nums[i]))

            i += 1
        return result
        
            
            
            
            


        