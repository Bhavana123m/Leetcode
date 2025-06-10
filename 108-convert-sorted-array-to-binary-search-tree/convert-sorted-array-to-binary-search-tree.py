# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
        def createNode(nums, start, end):
            if start> end:
                return
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = createNode(nums, start, mid-1)
            root.right = createNode(nums, mid+1, end)
            return root
        
        if not nums:
            return None
        start = 0
        nums_len = len(nums)
        end = nums_len - 1
        return createNode(nums, start, end)