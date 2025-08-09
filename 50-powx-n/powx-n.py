class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x = 1/x
            n=-n
        def power(base, exp):
            if exp == 0:
                return 1
            half = power(base, exp//2)
            if exp%2 == 0:
                return half*half
            return base*half*half
        return power(x, n)

        
        
        
        
        
        if n == 0:
            return 1
        sign = n/abs(n)
        product = 1
        n = abs(n)
        while n>0:
            product*= x
            n-=1
        if sign == -1:
            return 1/product
        return product