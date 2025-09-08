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
        # ------------------------------------ LCA I---------------------------------
        # if root is None:
        #     return None
        # if p.val == root.val or q.val == root.val:
        #     return root
        # left_tree_common = self.lowestCommonAncestor(root.left, p, q)
        # right_tree_common = self.lowestCommonAncestor(root.right, p, q)
        # if left_tree_common and right_tree_common:
        #     return root
        # if left_tree_common:
        #     return left_tree_common
        # if right_tree_common:
        #     return right_tree_common

        # -------------------------------------LCA I(Simplified) -----------------------------------
        
        # if not root or root.val == p.val or root.val == q.val:
        #     return root
        # left = lowestCommonAncestor(root.left, p, q)
        # right = lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root
        # return left or right

        # -------------------------------------LCA II(Simplified) -----------------------------------

        if not root:
            return None
        found = [False, False]
        # if p is q:
        #      return p if exists(root, p) else None

        
        def dfs(node):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if node is p:
                found[0] = True
                return node
            if node is q:
                found[1] = True
                return node
            if left and right:
                return node
            return left or right
        
        # def exists(root, target):
        #     if not root:
        #         return False
        #     if root is target:
        #         return True
        #     return exists(root.left, target) or exists(root.right, target)
        
        
        ancestor = dfs(root)
        # print(ancestor)
        # print(found)
        if found[0] and found[1]:
            return ancestor
        return None















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

