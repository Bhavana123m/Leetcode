class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator:
            return "0"
        # result_list = []
        # if (numerator < 0) != (denominator < 0):
        #     result_list.append("-")
        # result = float(abs(numerator))/abs(denominator)
        # res = str(result).split(".")
        # fraction_part = res[1]
        # real_part = res[0]
        # result_list.append(real_part)
        result = []
        
        if (numerator < 0) != (denominator < 0):
            result.append("-")

        num = abs(numerator)
        den = abs(denominator)

        result.append(str(num // den))
        num %= den

        if not num:
            return "".join(result)

        result.append(".")
        seen = {}

        # print(result)
        while num:
            if num in seen:
                result.insert(seen[num], "(")
                result.append(")")
                break
            seen[num] = len(result)
            num *= 10
            # print(num)
            # print(den)
            result.append(str(num // den))
            # print(result)
            num %= den
            # print(num)

        return "".join(result)



        