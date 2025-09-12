# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def dfs(node):
            if not node:
                return (0,0,0)
            left_tot, left_cnt, left_match = dfs(node.left)
            right_tot, right_cnt, right_match = dfs(node.right)

            total = left_tot + right_tot + node.val
            total_count = left_cnt + right_cnt + 1

            avg = total // total_count

            if avg == node.val:
                return (total, total_count, left_match + right_match + 1)
            else:
                return (total, total_count, left_match + right_match)

        return dfs(root)[2]
