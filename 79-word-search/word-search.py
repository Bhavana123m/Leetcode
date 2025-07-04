class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row<0 or row>=rows or col<0 or col>=cols or board[row][col]!=word[index]:
                return False
            visited = board[row][col]
            board[row][col] = ''
            if dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col-1, index+1) or dfs(row, col+1, index+1):
                return True
            board[row][col] = visited
        

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False


        # rows = len(board)
        # cols = len(board[0])
        # def dfs(row, col, index):
        #     if index == len(word):
        #         return True
            
        #     if row<0 or row>=rows or col<0 or col>=cols:
        #         return False

        #     if board[row][col] == word[index]:
        #         print(board[row][col])
        #         index+=1
        #         visted[]
        #         return dfs(row-1, col, index) or dfs(row+1, col, index) or dfs(row, col-1, index) or dfs(row, col+1, index)
            
        #     visted[

        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] == word[0]:
        #             if dfs(row-1, col, 1) or dfs(row+1, col, 1) or dfs(row, col-1, 1) or dfs(row, col+1, 1):
        #                 return True
        # return False
                

        # rows = len(board)
        # cols = len(board[0])
        # directions = [(-1,0),(1,0),(0,-1),(0,1)]
        # queue = deque()

        # def bfs(row, col, i):
        #     print("J")
        #     queue.append((row, col))
        #     while queue:
        #         # for _ in range(len(queue)):
        #         row, col = queue.popleft()
        #         for dr, dc in directions:
        #             if i<len(word):
        #                 new_row = row+dr
        #                 new_col = col + dc
        #                 if 0<=new_row<rows and 0<=new_col<cols and board[new_row][new_col] == word[i]:
        #                     print(i)
        #                     print("Ji")
        #                     queue.append((new_row, new_col))
        #                     i+=1
        #                     print(i)
        #     print(i)
        #     if i == len(word) - 1:
        #         return True
        
        # result = False
        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] == word[0]:
        #             result = bfs(row, col, 1)
        #             if result:
        #                 return result
        
        # return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != word[idx]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))
            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
    