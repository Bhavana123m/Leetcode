class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # For sides a ≤ b ≤ c, the triangle inequality reduces to a + b > c.
        # If we sort nums, we can fix the largest side c and count how many pairs (a,b) satisfy this.
        # Sort nums ascending.
        # For each index k from right to left (treat nums[k] as c):
        # Set i = 0, j = k - 1.
        # While i < j:
        # If nums[i] + nums[j] > nums[k], then all pairs with this j and any i' ∈ [i, j-1] work (because array is sorted). 
        # Add j - i and decrement j.
        # Else increment i.
        nums.sort()
        n = len(nums)
        count = 0
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i   # all (i..j-1, j, k) are valid
                    j -= 1
                else:
                        i += 1
        return count
