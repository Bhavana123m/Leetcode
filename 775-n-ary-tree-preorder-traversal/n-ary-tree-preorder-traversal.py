"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        arr = []
        self.dfs(root, arr)
        return arr
        
    def dfs(self, node, arr):
        if not node:
            return
        arr.append(node.val)
        for child in node.children:
            self.dfs(child, arr)

        