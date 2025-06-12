class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        seen = []
        for i in nums:
            if i not in seen:
                seen.append(i)
                count+=1
        nums[:] = seen
        return count

        
        
        
        
        
        
        
        
        
        
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
