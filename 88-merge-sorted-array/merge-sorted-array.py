class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        # if m == 0:
        #     return nums2
        i = m-1  #0
        j = n-1  #0
        k = n+m-1 #1
        while j>=0:   #1
            # print("Hi")
            # print(nums1[i])
            
            if i>=0 and nums2[j]<=nums1[i]: # 0>=0 and nums2[0]<=nums1[o] 1<=2 true
                nums1[k] = nums1[i]   # nums1[1] = nums1[0] = 2   nums1 = [2,2]
                i-=1
            else:  #0>=0 and nums2[0]>nums1[0]   1>2 wro
                # print(nums1[i])
                nums1[k] = nums2[j]
                j-=1
            k-=1
        return nums1





































        if n == 0 :
            return 
        # for i in range(nums1):
        #     for j in range(nums2):
        #         if nums1[i]>=nums2[j]:
        #             nums1[i]
        nums1[m:] = nums2
        nums1.sort()

