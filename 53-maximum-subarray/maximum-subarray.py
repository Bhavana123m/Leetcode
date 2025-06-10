class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        n = len(nums)
        total = float('-inf')
        for i in range(n):
            total = max(total + nums[i], nums[i])
            ans = max(total, ans)
        return ans