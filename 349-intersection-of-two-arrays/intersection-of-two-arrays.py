class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Two Pointers
        common = []
        nums1_no_dup = list(set(nums1))
        nums2_no_dup = list(set(nums2))
        nums1_no_dup.sort()
        nums2_no_dup.sort()

        i = 0
        j = 0
        while i<len(nums1_no_dup) and j<len(nums2_no_dup):
            if nums1_no_dup[i]<nums2_no_dup[j]:
                i+=1
            elif nums1_no_dup[i]>nums2_no_dup[j]:
                j+=1
            else:
                common.append(nums1_no_dup[i])
                i+=1
                j+=1
        return common

        # inbuilt 
        return list(set(nums1) & set(nums2))
        
        # Search in one set O(n)
        common = []
        nums1_no_dup = list(set(nums1))
        nums2_no_dup = list(set(nums2))
        for i in nums1_no_dup:
            if i in set(nums2_no_dup):
                common.append(i)
        return common