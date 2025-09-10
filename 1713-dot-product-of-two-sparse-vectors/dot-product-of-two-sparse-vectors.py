class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = []
        for i in range(len(nums)):
            ch = nums[i]
            if ch!=0:
                self.nums.append((i, ch))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        p1, p2 = 0, 0
        total = 0
        nums1, nums2 = self.nums, vec.nums

        while p1 < len(nums1) and p2 < len(nums2):
            idx1, val1 = nums1[p1]
            idx2, val2 = nums2[p2]

            if idx1 == idx2:
                total += val1 * val2
                p1 += 1
                p2 += 1
            elif idx1 < idx2:
                p1 += 1
            else:
                p2 += 1

        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)