class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rty
        pe: int
        """
        if x== 0:
            return 0
        low = 1
        high = x
        while low<=high:
            mid = (low+high)//2
            product = mid * mid
            if product == x:
                return mid
            elif product>x:
                high = mid-1
            else:
                low = mid+1
        return high
