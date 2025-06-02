class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = {}
        def dfs(index, target):
            if (index, target) not in res:
                if index == len(nums):
                    count = 1 if target == 0 else 0
                else:
                    count = dfs(index+1, target-nums[index]) + dfs(index+1, target+nums[index])
                res[(index, target)] = count
            return res[(index, target)]          
          
        return dfs(0, target)


    #     return self.cal(nums, target, 0, 0)
    
    # def cal(self, nums, tar, index, currSum):
    #     if index == len(nums):
    #         return 1 if currSum == tar else 0

    #     add = self.cal(nums, tar, index + 1, currSum + nums[index])
    #     sub = self.cal(nums, tar, index + 1, currSum - nums[index])

    #     return add + sub