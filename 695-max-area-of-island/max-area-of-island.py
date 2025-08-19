class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            area = 0
            queue = deque()
            queue.append((row, col))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                row, col = queue.popleft()
                if grid[row][col] == 0:
                    continue
                grid[row][col] = 2
                # area+=1
                for dr, dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]!=2 and grid[new_row][new_col]==1:
                        grid[new_row][new_col] = 2
                        area+=1
                        queue.append((new_row,new_col))
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ar = bfs(row, col) +  1
                    max_area = max(ar, max_area)
        
        return max_area

        