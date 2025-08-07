class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        end = 0
        while end < len(nums):
            start = end
            while end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1
            if start == end:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start]) + "->" + str(nums[end]))

            end += 1
        return result
        
            
            
            
            


        