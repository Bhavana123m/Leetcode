# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        tree_leafs1=[]
        tree_leafs2=[]
        self.postorder(root1, tree_leafs1)
        self.postorder(root2, tree_leafs2)
        len1 = len(tree_leafs1)
        len2 = len(tree_leafs2)
        if len1 != len2:
            return False
        for i in range(len1):
            if tree_leafs1[i] != tree_leafs2[i]:
                return False
        return True

    def postorder(self, node, leaf):
        if not node:
            return
        self.postorder(node.left, leaf)
        if not node.left and not node.right:
            leaf.append(node.val)
        self.postorder(node.right, leaf)

