# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Flip the tree so that:
        # The leftmost node becomes the new root.
        # For each original node:
        #   left.left  <- original right
        #   left.right <- original node
        # Original node's left/right set to None to avoid cycles.
        if root is None or root.left is None:
            return root  # leftmost node becomes new root
        new_root = self.upsideDownBinaryTree(root.left)
        # rewire under root.left (which survives in the new tree)
        root.left.left = root.right
        root.left.right = root

        # sever old links
        root.left = None
        root.right = None
        return new_root


        