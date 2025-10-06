class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return 0

        m = len(board)
        n = len(board[0])
        ships = 0

        r = 0
        while r < m:
            c = 0
            while c < n:
                if board[r][c] == 'X':
                    # Check there is no 'X' directly above
                    up_is_x = (r > 0 and board[r - 1][c] == 'X')
                    # Check there is no 'X' directly to the left
                    left_is_x = (c > 0 and board[r][c - 1] == 'X')
                    # Only count the head: no 'X' above and no 'X' left
                    if not up_is_x and not left_is_x:
                        ships += 1
                c += 1
            r += 1

        return ships
