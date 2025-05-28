# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        if root is None:
            return arr
        self.inorder(arr, root)
        return arr

    def inorder(self, arr, root):
        if root is None:
            return
        self.inorder(arr, root.left)
        arr.append(root.val)
        self.inorder(arr, root.right)
        