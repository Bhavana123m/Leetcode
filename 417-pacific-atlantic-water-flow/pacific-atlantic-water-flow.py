class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        pacific_ocean = [[False]*cols for _ in range(rows)]
        atlantic_ocean = [[False]*cols for _ in range(rows)]
        pacific_land = []
        atlantic_land = []
        for c in range(cols):
            pacific_land.append((0,c))
            atlantic_land.append((rows-1, c))
        for r in range(rows):
            pacific_land.append((r,0))
            atlantic_land.append((r, cols-1))
        def bfs(land, ocean):
            q = deque(land)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<rows and 0<=nc<cols and heights[r][c]<=heights[nr][nc] and not ocean[nr][nc]:
                        q.append((nr, nc))              
        
        bfs(pacific_land, pacific_ocean)
        bfs(atlantic_land, atlantic_ocean)
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific_ocean[i][j] and atlantic_ocean[i][j]:
                    res.append((i,j))
        return res
        

