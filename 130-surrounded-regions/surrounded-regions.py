class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        rows = len(board)
        cols = len(board[0])

        queue = deque()

        for row in range(rows):
            if board[row][0] == 'O':
                queue.append((row, 0))
            if board[row][cols-1] == 'O':
                queue.append((row, cols-1))
        for col in range(cols):
            if board[0][col] == 'O':
                queue.append((0, col))
            if board[rows-1][col] == 'O':
                queue.append((rows-1, col))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            row, col = queue.popleft()
            board[row][col] = '#'
            for dr, dc in directions:
                new_row =row+dr
                new_col = col+dc
                if 0<=new_row<rows and 0<=new_col<cols and board[new_row][new_col] != '#' and board[new_row][new_col] == 'O':
                    queue.append((new_row, new_col))
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'








































        # if not board:
        #     return board
        # rows = len(board)
        # cols = len(board[0])

        # def dfs(row, col):
        #     if row<0 or row>=rows or col<0 or col>=cols or board[row][col] != 'O':
        #         return
        #     board[row][col] = '#'
        #     dfs(row+1, col)
        #     dfs(row-1, col)
        #     dfs(row, col+1)
        #     dfs(row, col-1)

        # for row in range(rows):
        #     if board[row][0] == 'O':
        #         dfs(row,0)
        #     if board[row][cols-1] == 'O':
        #         dfs(row, cols-1)
        # for col in range(cols):
        #     if board[0][col] == 'O':
        #         dfs(0, col)
        #     if board[rows-1][col] == 'O':
        #         dfs(rows-1, col)
        
        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] == 'O':
        #             board[row][col] ='X'
        #         elif board[row][col] == '#':
        #             board[row][col] ='O'

