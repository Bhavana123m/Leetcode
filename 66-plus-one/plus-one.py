class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # https://leetcode.com/problems/plus-one/solutions/5360501/python-100-beat-100-efficient-optimal-solution-easy-to-understand
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i]+=1
                return digits
        return [1] + digits
        
        
        num_str = ""
        for digit in digits:
            num_str+=str(digit)
        result_str = str(int(num_str)+1)
        result = list(result_str)
        return [int(d) for d in result]

        