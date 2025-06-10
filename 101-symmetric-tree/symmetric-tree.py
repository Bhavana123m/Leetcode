# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        q = [root]
        while q:
            level = []
            q_len = len(q)
            while q_len:
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
                # level.append(node.val)
                q_len -= 1
            if level != level[::-1]:
                return False
        return True
