# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/find-leaves-of-binary-tree/solutions/6201761/postorder-delete-each-leaf-after-collect-y651
        if not root:
            return []
        
        res = []
        def prune(node):
            if not node:
                return None
            if not node.left and not node.right:
                step_vals.append(node.val)
                return None #Delete leaf
            node.left = prune(node.left)
            node.right = prune(node.right)
            return node

        while root:
            step_vals = []
            root = prune(root)
            res.append(step_vals)
        
        return res