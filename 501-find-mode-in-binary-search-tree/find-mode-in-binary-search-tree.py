# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.max_cnt = 0
        self.cnt = 0
        self.seen = None
        self.result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.seen == node.val:
                self.cnt+=1
            else:
                self.cnt =1
                self.seen = node.val
            if self.cnt > self.max_cnt:
                self.max_cnt = self.cnt
                self.result = [node.val]
            elif self.cnt == self.max_cnt:
                self.result.append(node.val)
            inorder(node.right)
        inorder(root)
        return self.result