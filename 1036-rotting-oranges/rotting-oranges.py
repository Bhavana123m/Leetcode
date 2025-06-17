class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        time = 0
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh+=1
        rot = 0
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while q:
            #  print(q)
             r,c,t = q.pop(0)
             time = max(time, t)
             for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))
                    rot += 1

        if rot == fresh:
            return time
        return -1