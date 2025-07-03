class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            if queue:
                time += 1
        return time if fresh == 0 else -1


        
















        # n = len(grid)
        # m = len(grid[0])
        # fresh = 0
        # time = 0
        # q = []
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 2:
        #             q.append((i,j,0))
        #         elif grid[i][j] == 1:
        #             fresh+=1
        # rot = 0
        # directions = [(-1,0), (0,1), (1,0), (0,-1)]

        # while q:
        #     #  print(q)
        #      r,c,t = q.pop(0)
        #      time = max(time, t)
        #      for dr, dc in directions:
        #         nr, nc = r + dr, c + dc
        #         if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
        #             grid[nr][nc] = 2
        #             q.append((nr, nc, t+1))
        #             rot += 1

        # if rot == fresh:
        #     return time
        # return -1