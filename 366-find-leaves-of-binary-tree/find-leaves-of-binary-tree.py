# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/find-leaves-of-binary-tree/solutions/6201761/postorder-delete-each-leaf-after-collect-y651
        res = []
        def dfs(node):
            # Returns (pruned_node, round_removed)
            if node is None:
                return None, -1

            # Postorder: process children first
            left_node, left_round = dfs(node.left)
            right_node, right_round = dfs(node.right)

            # Keep whatever remains after pruning below (will be None once removed)
            node.left, node.right = left_node, right_node

            # This node’s removal round is one more than the max of its children’s rounds
            my_round = max(left_round, right_round) + 1

            # Ensure bucket exists, then record this node
            if my_round == len(res):
                res.append([])
            res[my_round].append(node.val)

            # Delete this node in this round by returning None upward
            return None, my_round

        # After dfs, the entire tree has been deleted (root becomes None)
        dfs(root)
        return res
        
        
        
        if not root:
            return []
        
        res = []
        def prune(node):
            if not node:
                return None
            if not node.left and not node.right:
                step_vals.append(node.val)
                return None #Delete leaf
            node.left = prune(node.left)
            node.right = prune(node.right)
            return node

        while root:
            step_vals = []
            root = prune(root)
            res.append(step_vals)
        
        return res