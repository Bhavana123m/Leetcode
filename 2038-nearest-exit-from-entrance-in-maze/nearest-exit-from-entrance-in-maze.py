class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows = len(maze)
        cols = len(maze[0])
        queue = deque()

        for i in range(rows):
            if maze[i][0] == '.' and [i,0]!=entrance:
                queue.append((i,0))
            if maze[i][cols-1] == '.' and [i,cols-1]!=entrance:
                queue.append((i,cols-1))
        for i in range(cols):
            if maze[0][i] == '.' and [0,i]!=entrance:
                queue.append((0,i))
            if maze[rows-1][i] == '.' and [rows-1,i]!=entrance:
                queue.append((rows-1, i))
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if maze[row][col] == '+':
                    continue
                maze[row][col] = '#'
                directions = [(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if 0<=new_row<rows and 0<=new_col<cols and maze[new_row][new_col]!='+' and maze[new_row][new_col]=='.':
                        if [new_row,new_col] == entrance:
                            return steps+1
                        maze[new_row][new_col] = '#'
                        queue.append((new_row, new_col))

            steps+=1
        return -1

