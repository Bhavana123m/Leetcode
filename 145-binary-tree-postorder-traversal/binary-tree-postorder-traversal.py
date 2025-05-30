# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        if root is None:
            return arr
        self.postorder(arr, root)
        return arr
    def postorder(self, arr, root):
        if root is None:
            return
        self.postorder(arr, root.left)
        self.postorder(arr, root.right)
        arr.append(root.val)
