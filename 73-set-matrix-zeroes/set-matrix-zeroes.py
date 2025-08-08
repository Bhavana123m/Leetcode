class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        rows = len(matrix)
        columns  = len(matrix[0])
        rows_arr = [False]*rows
        cols_arr = [False]*columns
        # print(rows_arr)
        # print(cols_arr)
        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0:
                    rows_arr[row] = True
                    cols_arr[col] = True
        # print(rows_arr)
        # print(cols_arr)
        for row in range(rows):
            for col in range(columns):
                if rows_arr[row] or cols_arr[col]:
                    matrix[row][col] = 0
        # print(matrix)
                