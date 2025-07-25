"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth+1



        
        
        
        if not root:
            return 0
        if not root.children:
            return 1
        heights = []
        for node in root.children:
            heights.append(self.maxDepth(node))
        return max(heights) + 1
