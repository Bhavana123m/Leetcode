# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def postorder(node):
            if not node:
                return 0, 0
            left_sum, left_tilt = postorder(node.left)
            right_sum, right_tilt = postorder(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt = tilt + left_tilt + right_tilt
            return left_sum + right_sum + node.val , total_tilt
        
        tilt_sum = postorder(root)[1]
        return tilt_sum
















        self.tilt_sum = 0
        def postorder(node):
            if not node:
                return 0
            left_sum = postorder(node.left)
            right_sum = postorder(node.right)
            self.tilt_sum+=abs(left_sum - right_sum)
            return left_sum + right_sum + node.val
        postorder(root)
        return self.tilt_sum

