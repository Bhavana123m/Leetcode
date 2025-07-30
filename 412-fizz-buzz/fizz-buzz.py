class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer  = []
        for i in range(n):
            element = i+1
            if element%15 ==0 :
                answer .append("FizzBuzz")
            elif element%5 ==0 :
                answer .append("Buzz")
            elif element%3 ==0 :
                answer .append("Fizz")
            else:
                answer.append(str(element))
        return answer
