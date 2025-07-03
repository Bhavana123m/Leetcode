"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
import math
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # if not root:
        #     return []
        # max_per_level_list = []
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     q_len = len(queue)
        #     max_node_level = float('-inf')
        #     for _ in range(q_len):
        #         node = queue.popleft()
        #         max_node_level = max(node.val, max_node_level)
        #         if node.children:
        #             for child in node.children:
        #                 queue.append(child)
        #     max_per_level_list.append(max_node_level)
        # return max_per_level_list


















        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            q_len = len(queue)
            level = []
            for _ in range(q_len):
                node = queue.popleft()
                if node.children:
                    for child in node.children:
                        queue.append(child)
                level.append(node.val)
            result.append(level)
        return result