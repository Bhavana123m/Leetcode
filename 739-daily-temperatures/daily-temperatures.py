class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [0]*len(temperatures)
    
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack.pop()
                output[top] = i - top
            stack.append(i)
        return output

            
