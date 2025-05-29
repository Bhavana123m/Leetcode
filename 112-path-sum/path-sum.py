# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        total = 0
        return self.path_sum(root, targetSum, total)
        
    def path_sum(self, root, targetSum, total):
        if root is None:
            return False
        if root.left is None and root.right is None:
            total += root.val
            if total == targetSum:
                return True
        return self.path_sum(root.left, targetSum, total + root.val) or self.path_sum(root.right, targetSum, total + root.val)