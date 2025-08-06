class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0 or num < 10:
            return num
        total = 0
        while num>0:
            total+=num%10
            num = num//10
        return self.addDigits(total)