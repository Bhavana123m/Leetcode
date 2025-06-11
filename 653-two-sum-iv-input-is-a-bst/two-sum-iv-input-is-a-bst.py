# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()
        return self.find_seen(root, seen, k)

    def find_seen(self, node, seen, target):
        if not node:
            return False
        if (target - node.val) in seen:
            return True
        seen.add(node.val)
        return self.find_seen(node.left, seen, target) or self.find_seen(node.right, seen, target)
