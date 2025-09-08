# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        left_tree_common = self.lowestCommonAncestor(root.left, p, q)
        right_tree_common = self.lowestCommonAncestor(root.right, p, q)
        if left_tree_common and right_tree_common:
            return root
        if left_tree_common:
            return left_tree_common
        if right_tree_common:
            return right_tree_common
















        if root is None:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right

