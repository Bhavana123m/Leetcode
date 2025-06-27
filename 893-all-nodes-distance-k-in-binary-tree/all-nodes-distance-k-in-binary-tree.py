# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        adj_list = defaultdict(list)
        def build_graph(node, parent=None):
            if not node:
                return
            if parent:
                adj_list[node].append(parent)
                adj_list[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
        build_graph(root)
        queue = deque()
        visited = set()
        queue.append(target)
        visited.add(target)
        result = []
        distance = 0
        while queue:
            level = len(queue)
            for _ in range(level):
                if distance == k:
                    return [node.val for node in queue]
                node = queue.popleft()
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            distance+=1
        return result
                    