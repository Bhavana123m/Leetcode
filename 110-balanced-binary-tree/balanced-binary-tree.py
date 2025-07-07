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
        if not root:
            return True
        def check_height(node):
            if not node:
                return 0
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            if abs(right_height-left_height)>1:
                return -1
            return 1+max(right_height, left_height)
        
        return check_height(root) != -1






































































        def height_check(node):
            if not node:
                return 0
            left_height = height_check(node.left)
            if (left_height == -1):
                return -1
            right_height = height_check(node.right)
            if (right_height == -1):
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        
        return height_check(root)!=-1