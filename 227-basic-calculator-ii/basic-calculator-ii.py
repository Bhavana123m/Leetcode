class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def precedence(c):
            return c == '*' or c == '/'

        op, num, cur = deque(), deque(), 0
        for c in s + '#':
            if c == ' ': continue
            elif c.isdigit():
                cur = cur * 10 + int(c)
            else:
                num.append(cur)
                while op and precedence(c) <= precedence(op[-1]):
                    num1, num2, curOp = num.pop(), num.pop(), op.pop()
                    if   curOp == '*': num.append(num2 * num1)
                    elif curOp == '/': num.append(num2 // num1)
                    elif curOp == '+': num.append(num2 + num1)
                    elif curOp == '-': num.append(num2 - num1)
                op.append(c)
                cur = 0
    
        return num.pop()




        def precedence(c):
            return c == '*' or c == '/'
        def toPostfix(s):
            op, post = deque(), ''
            for c in s:
                if c == ' ': continue
                elif c.isdigit(): post += c
                else:
                    post += '|'
                    while op and precedence(c) <= precedence(op[-1]):
                        post += op.pop()
                    op.append(c)
                    
            return post + '|' + ''.join(reversed(op))
        
        s, num, i = toPostfix(s), deque(), 0
        while i < len(s):
            if s[i].isdigit():
                j = s.find('|', i+1)
                num.append(int(s[i:j]))
                i = j
            else:
                num1, num2 = num.pop(), num.pop()
                if   s[i] == '*': num.append(num2 * num1)
                elif s[i] == '/': num.append(num2 // num1)
                elif s[i] == '+': num.append(num2 + num1)
                elif s[i] == '-': num.append(num2 - num1)
            i += 1

        return num.pop()
        