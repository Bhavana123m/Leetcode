# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        maxi = -float('inf')
        
        def check(node, maxi):
            if not node:
                return
            if node.val >= maxi:
                maxi = node.val
                self.count+=1
            check(node.left, maxi) 
            check (node.right, maxi)
        check(root, maxi)
        return self.count
        



