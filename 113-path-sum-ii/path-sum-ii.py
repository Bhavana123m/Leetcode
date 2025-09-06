# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        def calculate_paths(node, result, path):
            if not node:
                return
            path.append(node.val)
            total = sum(path)
            if node.left is None and node.right is None:
                if total == targetSum:
                    result.append(path[:])

            else:
                calculate_paths(node.left, result, path)
                calculate_paths(node.right, result, path)
            path.pop()
        
        calculate_paths(root, result, [])
        return result
        
