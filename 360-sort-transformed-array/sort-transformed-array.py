class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
       
#         Key idea: a quadratic is a parabola. Use two pointers instead of mapping+sorting.

# If a ≥ 0 (opens up), values at the ends are largest; fill result from the end downward.

# If a < 0 (opens down), values at the ends are smallest; fill result from the start upward.

# This works even when a = 0 (linear): it naturally handles increasing/decreasing by comparisons.
        # if parabola opens upwards (a >= 0), fill from the end
        # if parabola opens downwards (a < 0), fill from the start
        


        def f(x):
            return a*x*x + b*x + c
        
        n = len(nums)
        res = [0]*n
        i = 0
        j = n-1
        if a>=0:
            k = n-1 # Keep pointer at last of result as valu is bigger for upper parabola
            while i<=j:
                left, right = f(nums[i]), f(nums[j])
                if left >= right:
                    res[k] = left
                    i += 1
                else:
                    res[k] = right
                    j -= 1
                k -= 1
        else:
            k = 0
            while i <= j:
                left, right = f(nums[i]), f(nums[j])
                if left <= right:
                    res[k] = left
                    i += 1
                else:
                    res[k] = right
                    j -= 1
                k += 1
        return res
            


            