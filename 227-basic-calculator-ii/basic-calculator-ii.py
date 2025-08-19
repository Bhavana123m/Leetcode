class Solution(object):
    def calculate(self, s):
        # Helper: integer division truncating toward 0
        def div_trunc_zero(a, b):
            q = abs(a) // abs(b)
            return q if a * b >= 0 else -q

        stack = []
        num = 0
        sign = '+'

        # Append sentinel operator to flush the last number
        s = s.strip() + '+'
        i = 0
        n = len(s)

        while i < n:
            ch = s[i]

            if ch == ' ':
                i += 1
                continue

            if '0' <= ch <= '9':
                num = num * 10 + (ord(ch) - 48)
            elif ch in '+-*/':
                # Apply the previous sign with the number we've built
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:  # sign == '/'
                    prev = stack.pop()
                    stack.append(div_trunc_zero(prev, num))

                # Update to the new sign and reset number
                sign = ch
                num = 0
            # (No other characters expected per problem statement)

            i += 1

        return sum(stack)


# class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         stack = []
#         num = 0
#         prev_op = '+'
#         n = len(s)
        
#         for i in range(n):
#             if s[i].isdigit():
#                 num = num * 10 + int(s[i])
#             if (not s[i].isdigit() and s[i] != ' ') or i == n - 1:
#                 if prev_op == '+':
#                     stack.append(num)
#                 elif prev_op == '-':
#                     stack.append(-num)
#                 elif prev_op == '*':
#                     stack.append(stack.pop() * num)
#                 elif prev_op == '/':
#                     # Handle division truncating toward zero
#                     top = stack.pop()
#                     if top // num < 0 and top % num != 0:
#                         stack.append(top // num + 1)
#                     else:
#                         stack.append(top // num)
#                 prev_op = s[i]
#                 num = 0
        
#         return sum(stack)