class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)

        # If even after the last element we still haven't reached k missings
        if arr[-1] - n < k:
            return k + n

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            # how many missing up to arr[mid]
            miss = arr[mid] - (mid + 1)
            if miss < k:
                left = mid + 1
            else:
                right = mid
        return left + k
        
        prev = 0
        for x in arr:
            gap = x - prev - 1
            if k<=gap:
                return prev+k
            k-=gap
            prev = x
        return prev+k