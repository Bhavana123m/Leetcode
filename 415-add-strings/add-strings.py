class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1)-1
        j = len(num2) - 1
        carry = 0
        res = []
        while i>=0 or j>=0 or carry:
            if i>=0:
                d1 = ord(num1[i]) - ord('0')
            else:
                d1 = 0
            if j>=0:
                d2 = ord(num2[j]) - ord('0')
            else:
                d2 = 0
            
            s = d1+d2+carry
            res.append(str(s%10))
            carry = s//10
            i-=1
            j-=1
        return "".join(res[::-1])