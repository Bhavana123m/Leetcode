class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 1
        lis = []
        for n in nums:
            if lis and lis[len(lis)-1]<n:
                lis.append(n)
            elif not lis:
                lis.append(n)
            elif lis and lis[len(lis)-1]>n:
                low = 0
                high = len(lis)-1
                while low<high:
                    mid = (low+high)//2
                    if lis[mid] == n:
                        break
                    elif lis[mid] < n:
                        low = mid + 1
                    else:
                        high = mid
                if low == high and lis[high]>n:
                    lis[high] = n
                elif lis[mid] == n:
                    lis[mid] = n

        return len(lis)
            




















        # tails = [0] * len(nums)
        # size = 0
        # for x in nums:
        #     i, j = 0, size
        #     while i != j:
        #         m = (i + j) / 2
        #         if tails[m] < x:
        #             i = m + 1
        #         else:
        #             j = m
        #     tails[i] = x
        #     size = max(i + 1, size)
        # return size