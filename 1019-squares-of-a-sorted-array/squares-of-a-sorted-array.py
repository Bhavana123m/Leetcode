class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # left = 0
        # right = n - 1
        # fill_pos = n - 1  # position to fill from the end

        # while left <= right:
        #     if abs(nums[left]) > abs(nums[right]):
        #         nums[fill_pos] = nums[left] * nums[left]
        #         left += 1
        #     else:
        #         nums[fill_pos] = nums[right] * nums[right]
        #         right -= 1
        #     fill_pos -= 1

        # return nums




# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
        n = len(nums)
        left = 0
        right = n-1
        arr = [0]*n
        for i in range(n-1, -1, -1):
            if abs(nums[left])>abs(nums[right]):
                arr[i] = nums[left]*nums[left]
                left+=1
            else:
                arr[i] = nums[right]*nums[right]
                right-=1
        return arr


        # left = 0 
        # right = len(nums)-1

        # while left<=right:
        #     if abs(nums[left])<abs(nums[right]):
        #         nums[right] = nums[right]*nums[right]
        #         right-=1
        #     elif abs(nums[left])>abs(nums[right]):
        #         nums[left], nums[right] = nums[right], nums[left]
        #         nums[right] = nums[right]*nums[right]
        #         right-=1
        #     elif abs(nums[left])==abs(nums[right]):
        #         nums[right] = nums[right]*nums[right]
        #         right-=1
        # return nums

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        n = len(nums)
        ans = [0] * n
        start, end = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[start]) >= abs(nums[end]):
                ans[i] = nums[start] * nums[start]
                start += 1
            else:
                ans[i] = nums[end] * nums[end]
                end -= 1
        return ans
        