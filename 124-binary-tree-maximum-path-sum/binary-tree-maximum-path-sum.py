# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0
        ans = -float('inf')
        def maxsum(node, ans):
            if not node:
                return ans, 0
            ans, sum_left = maxsum(node.left, ans)
            ans, sum_right = maxsum(node.right, ans)
            node_val = node.val
            sum_node_best_l_r = node_val + max(sum_left, sum_right)
            sum_node_path = node_val + sum_left + sum_right
            ans = max(ans, node_val, sum_node_best_l_r, sum_node_path)
            return ans, max(node.val, sum_node_best_l_r)
        ans, _ = maxsum(root, ans)
        return ans