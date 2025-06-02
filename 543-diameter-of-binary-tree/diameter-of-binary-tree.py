# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0
        self.compute_depth(root)
        return self.max_diameter
    
    def compute_depth(self, root):
        if root is None:
            return 0
        else:
            left_depth = self.compute_depth(root.left)
            right_depth = self.compute_depth(root.right)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)