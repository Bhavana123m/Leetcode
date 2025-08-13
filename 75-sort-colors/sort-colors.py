class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Dutch algorithm
        low = 0
        high = len(nums)-1
        mid = 0
        while mid<=high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1




        cz,co,ct=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                cz+=1
            elif nums[i]==1:
                co+=1
            else:
                ct+=1
        index=0
        for _ in range(cz):
            nums[index]=0
            index+=1
        for _ in range(co):
            nums[index]=1
            index+=1
        for _ in range(ct):
            nums[index]=2
            index+=1