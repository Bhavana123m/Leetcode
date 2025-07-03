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
                    print("Hi")
                    count+=1
                    dfs(row, col)
        return count
