# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return TreeNode(val)

        # If the value to insert is less than the current node's value,
        # we need to insert it into the left subtree
        if val < root.val:
            # Recursively insert into the left subtree and update root.left
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Else (since duplicates don't exist), val > root.val, insert into right subtree
            root.right = self.insertIntoBST(root.right, val)

        # Return the root of this subtree so parent calls can link properly
        return root