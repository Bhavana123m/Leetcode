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
        high = (rows*cols)-1
        while low<=high:
            mid = (low+high)//2
            row = mid//cols
            col = mid%cols
            val = matrix[row][col]
            if target == val:
                return True
            elif val>target:
                high-=1
            else:
                low+=1
        return False




























































        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows*cols -1
        while low<=high:
            mid = (low+high)//2
            row = mid // cols
            col = mid % cols
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
        # def binary_search(low, high):
        #     if low > high:
        #         return False 
        #     mid = (low+high)//2
        #     row = mid // cols
        #     col = mid % cols
        #     mid_val = matrix[row][col]
        #     if mid_val == target:
        #         return True
        #     if mid_val>target:
        #         high = mid - 1
        #     elif mid_val<target:
        #         low = mid+1
        #     return binary_search(low, high)
            
        # return binary_search(low, high)