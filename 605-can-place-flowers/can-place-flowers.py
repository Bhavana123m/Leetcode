class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n ==0:
            return True

        zeroes =1 
        for i in range(len(flowerbed)):
            plot = flowerbed[i]
            if plot == 0:
                zeroes+=1
            else:
                alternate_empty = (zeroes - 1)//2

                n-=alternate_empty
                if n<=0:
                    return True
                zeroes = 0
        zeroes += 1
        alternate_empty = (zeroes - 1)//2
        n-=alternate_empty
        if n > 0:
            return False
        return True