class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                row, col = queue.popleft()
                if grid[row][col] == '0':
                    continue
                grid[row][col] = '2'
                for dr, dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]!='2' and grid[new_row][new_col]=='1':
                        grid[new_row][new_col] = '2'
                        queue.append((new_row,new_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count+=1
                    bfs(row, col)
        return count
                    
                    
        










        
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        count = 0
        def dfs(row, col):
            if row < 0 or row>=rows or col<0 or col>=cols or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(row+1, col)
            dfs(row-1,col)
            dfs(row, col+1)
            dfs(row,col-1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count+=1
                    dfs(row, col)
        return count
