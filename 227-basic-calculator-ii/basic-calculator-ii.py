class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        prev_op = '+'
        n = len(s)
        
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == n - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    # Handle division truncating toward zero
                    top = stack.pop()
                    if top // num < 0 and top % num != 0:
                        stack.append(top // num + 1)
                    else:
                        stack.append(top // num)
                prev_op = s[i]
                num = 0
        
        return sum(stack)