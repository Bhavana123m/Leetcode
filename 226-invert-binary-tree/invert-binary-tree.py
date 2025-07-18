# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        self.helper(root)
        return root
     
    def helper(self, root):
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.helper(root.left)
        self.helper(root.right)

        