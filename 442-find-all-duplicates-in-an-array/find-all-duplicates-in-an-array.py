class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0]*(len(nums)+1)
        res = []
        for num in nums:
            if arr[num]>0:
                res.append(num)
            else:
                arr[num]=1
        return res
        # result = []
        # prev = set()
        # for n in nums:
        #     if n in prev:
        #         result.append(n)
        #     else:
        #         prev.add(n)
        # return result