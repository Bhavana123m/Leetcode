class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        if not grid1 or not grid2:
            return 0
        rows = len(grid1)
        cols = len(grid1[0])
        sub_count = 0  

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            key = True
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if 0<=new_row<rows and 0<=new_col<cols and grid2[new_row][new_col]==1:
                        if grid1[new_row][new_col] != 1:
                            key = False
                        grid2[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            if key:
                return 1
            return 0



        for row in range(rows):
            for col in range(cols):
                if grid1[row][col] == 1 and grid2[row][col] == 1:
                    grid2[row][col] = 2
                    sub_count+= bfs(row, col)
        return sub_count
