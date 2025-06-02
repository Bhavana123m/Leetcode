# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        result = []
        self._dfs(root, "", result)
        return result

    def _dfs(self, node, path, result):
        if node:
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                path += '->'
                self._dfs(node.left, path, result)
                self._dfs(node.right, path, result)
        
