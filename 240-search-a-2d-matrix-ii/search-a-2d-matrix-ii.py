class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = cols-1
        while low<rows and high>=0:
            if matrix[low][high]== target:
                return True
            elif matrix[low][high]>target:
                high-=1
            else:
                low+=1
        return False
            