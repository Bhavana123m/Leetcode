from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        visited = set()
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        q = deque()
        q.append((0,0,1))
        while q:
            q_len = len(q)
            while q_len:
                x, y, path_len = q.popleft()
                q_len -= 1
                if x == n - 1 and y == n - 1:
                    return path_len
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and
                        grid[nx][ny] == 0 and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        q.append((nx, ny, path_len + 1))
        return -1

