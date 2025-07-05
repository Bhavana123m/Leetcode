class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        carry = 0
        l1 = len(a)
        l2 = len(b)
        while l1>0 or l2>0 or carry>0:
            total = carry
            if l1>0:
                total += int(a[l1-1])
                l1-=1
            if l2>0:
                total += int(b[l2-1])
                l2-=1
            carry = total//2
            s+=str(total%2)

        return s[::-1]
        












































        # return bin(int(a,2) + int(b,2))[2:]
        # int(a, 2) and int(b, 2) convert the binary strings a and b to decimal integers.
        # bin(sum)[2:] converts the result back to binary and slices off the '0b' prefix that bin() adds.
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = []
        while i>=0 or j>=0 or carry:
            total = carry
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total+=int(a[j])
                j-=1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(result[::-1])