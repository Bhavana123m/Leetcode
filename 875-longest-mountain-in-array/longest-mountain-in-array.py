class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n<3:
            return 0
        peak = 1
        max_len = 0

        while peak < n-1:
            if arr[peak-1]<arr[peak]>arr[peak+1]:
                start = peak-1
                end = peak+1
                while start > 0 and arr[start-1]<arr[start]:
                    start-=1
                while end < n-1 and arr[end]> arr[end+1]:
                    end+=1
                max_len = max(max_len, end-start+1)

                peak = end

            else:
                peak+=1
        
        return max_len


            

