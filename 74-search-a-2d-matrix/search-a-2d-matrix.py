class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        print(rows)
        print(cols)
        low = 0
        high = rows*cols -1
        def binary_search(low, high):
            if low > high:
                return False 
            mid = (low+high)//2
            row = mid // cols
            col = mid % cols
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            if mid_val>target:
                high = mid - 1
            elif mid_val<target:
                low = mid+1
            return binary_search(low, high)
            
        return binary_search(low, high)