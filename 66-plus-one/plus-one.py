class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_str = ""
        for digit in digits:
            num_str+=str(digit)
        result_str = str(int(num_str)+1)
        result = list(result_str)
        return [int(d) for d in result]

        