class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr)<3:
            return 0
        max_dist = 0
        peek = 1 # Peak is never first element so start from 2nd
        # while arr:
        while peek<len(arr):
            if peek < len(arr)-1 and arr[peek-1]<arr[peek] > arr[peek+1]:
                start = peek
                end = peek
                while start>0 and arr[start]>arr[start-1]:
                    start-=1
                while end< len(arr)-1 and arr[end]>arr[end+1]:
                    end+=1
                max_dist = max(max_dist, end - start+1)
            peek+=1
        return max_dist
            