class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # indx = -1
        # count = 0
        # n = len(nums)
        
        # # count the number of non-increasing elements
        # for i in range(n-1):
        #     if nums[i] >= nums[i+1]:
        #         indx = i
        #         count += 1
        
        # #the cases explained above
        # if count==0:
        #     return True
        
        # if count == 1:
        #     if indx == 0 or indx == n-2:
        #         return True
        #     if nums[indx-1] < nums[indx+1] or(indx+2 < n and nums[indx] < nums[indx+2]):
        #         return True
            
        # return False
        idx = -1
        count = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i]>=nums[i+1]:
                count+=1
                idx = i
        if count == 0:
            return True
        if count == 1:
            if idx == 0 or idx == n-2:
                return True
            if (nums[idx-1]<nums[idx+1]) or (idx+2<n and nums[idx]<nums[idx+2]):
                return True
            # if idx+2<n and nums[idx]<nums[idx+2]:
            #     return True
        return False                
        # k = 1
        # for i in range(1, len(nums)):
        #     if nums[i-1]<nums[i]:
        #         i+=1
        #     elif nums[i]<=nums[i-1]:
        #         print("high")
        #         print(nums[i])
        #         if k>0:
        #             nums[i],nums[i-1] = nums[i-1],nums[i]
        #             i+=1
        #             k-=1
        #         else:
        #             return False
        # return True
                