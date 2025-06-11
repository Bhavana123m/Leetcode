# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height_check(node):
            if node is None:
                return 0
            left_height = height_check(node.left)
            right_height = height_check(node.right)
            if (left_height == -1) or (right_height == -1):
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        if not root:
            return True
        
        return height_check(root)!=-1