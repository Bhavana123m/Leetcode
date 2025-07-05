# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return None
            node.left =  dfs(node.left)
            node.right = dfs(node.right)
            if not node.right and not node.left and node.val == target:
                return None
            return node
        return dfs(root)