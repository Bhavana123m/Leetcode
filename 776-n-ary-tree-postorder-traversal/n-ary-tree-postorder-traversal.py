"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        arr = []
        self.dfs(root, arr)
        return arr

    def dfs(self, node, arr):
        if not node:
            return
        for child in node.children:
            self.dfs(child, arr)
        arr.append(node.val)

