# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def calculateSum(node, is_left):
            if node is None:
                return 0
            if not node.left and not node.right:
               return node.val if is_left else 0
            return calculateSum(node.left, True) + calculateSum(node.right, False)
        return calculateSum(root, False)

        