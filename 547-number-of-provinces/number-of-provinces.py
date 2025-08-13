class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        if not isConnected:
            return 0
        n = len(isConnected)
        count = 0
        visited = set()

        def bfs(i):
            queue = deque()
            queue.append(i)
            visited.add(i)
            while queue:
                city = queue.popleft()
                for neighbor in range(n):
                    if isConnected[city][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)


        for i in range(n):
            if i not in visited:
                bfs(i)
                count+=1
        return count
                

        