"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        copy_graph = {}
        copy_graph[node] = Node(node.val)
        q = deque([node])
        while q:
            curr_node = q.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in copy_graph:
                    copy_graph[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                copy_graph[curr_node].neighbors.append(copy_graph[neighbor])
        return copy_graph[node]

