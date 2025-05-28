# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        # if root and root.left is None and root.right is None:
        #     return 1
        # q = [root]
        # while q:
        #     level_Count = 0
        #    
    #         q.pop(0)
                
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))
        