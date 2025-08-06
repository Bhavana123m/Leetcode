class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common = []
        nums1_no_dup = list(set(nums1))
        nums2_no_dup = list(set(nums2))
        for i in nums1_no_dup:
            if i in set(nums2_no_dup):
                common.append(i)
        return common