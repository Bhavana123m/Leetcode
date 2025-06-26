class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        # print(adj_list)
        # Using BFS
        visited = set()
        queue = [source]
        while queue:
            node = queue.pop()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False
