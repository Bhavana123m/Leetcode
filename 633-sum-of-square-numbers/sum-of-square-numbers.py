class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # If a² + b² = c, then both a and b must lie between 0 and √c.
        # Start with a = 0 (smallest candidate), b = floor(√c) (largest candidate).
        # Compute s = a² + b².
        # If s == c → found a valid pair → return True.
        # If s < c → sum too small → increase a to make it larger.
        # If s > c → sum too big → decrease b to make it smaller.
        # Continue until a > b.
        # We’re exploring all possible sums in increasing/decreasing order; no pair is missed.
        
        # Two pointers: smallest a, largest b
        a = 0
        b = int(math.sqrt(c))
        while a <= b:
            s = a*a + b*b
            if s == c:
                return True
            elif s < c:
                a += 1   # increase sum
            else:
                b -= 1   # decrease sum

        return False
        