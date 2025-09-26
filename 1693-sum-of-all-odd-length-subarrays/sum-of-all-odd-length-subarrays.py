class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Finf how many times an element will be in odd lenght window
        n = len(arr)
        total = 0
        i = 0
        while i<n:
            left = i+1
            right = n-i
            all_including_i = left * right
            odd_count = (all_including_i + 1) // 2
            total += arr[i] * odd_count
            i += 1

        return total




        # Not optimised
        total = 0
        n = len(arr)

        prefix = [0]*(n+1)

        for i in range(1,n+1):
            prefix[i] = arr[i-1] + prefix[i-1]
        odd_step = 1

        while odd_step <=n:
            for i in range(n-odd_step+1):
                total += prefix[i+odd_step] - prefix[i]
            odd_step+=2
        
        return total
