class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        next = 1
        for start in range(1, len(nums)):
            if nums[start]!=nums[start-1]:
                nums[next] = nums[start]
                next+=1
        return next

        
        
        
        
        
        
        
        
        
        
        count = 0
        prev = []
        for i in nums:
            if i not in prev:
                prev.append(i)
                count+=1
        nums[:] = prev
        return count
        
        
        
        nums[:] = sorted(set(nums))
        return len(nums)
