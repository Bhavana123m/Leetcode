class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        revered = 0
        while x != 0:
            digit = x%10
            x //= 10
            revered = revered * 10 + digit
            if revered >= (2**31 -1):
                return 0
        return sign * revered