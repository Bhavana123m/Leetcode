import math
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # q = [root]
        # while q:
        #     node = q.pop()
        #     # print(node)
        #     if node.left:
        #         if node.left.val > node.val or node.left.val == node.val:
        #             return False
        #         q.append(node.left)
        #     if node.right:
        #         if node.val > node.right.val or node.val == node.right.val:
        #             return False
        #         q.append(node.right)
        
        # return True
        return self._isValidBST(root, -math.inf, math.inf)

    def _isValidBST(self, node, min, max):
        if not node:
            return True
        if not (min < node.val < max):
            return False
        return self._isValidBST(node.left, min, node.val) and self._isValidBST(node.right, node.val, max)
        