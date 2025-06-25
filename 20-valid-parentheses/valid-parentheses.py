

class Solution(object):
    def isValid(self, str):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map ={')':'(', '}':'{',']':'['}
        for char in str:
            if char in map:
                if not stack or map[char]!=stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
            
        # s = []
        # for char in str:
        #     if char in '[{(':
        #         s.append(char)
        #     else:
        #         if len(s) == 0:
        #             return False
        #         else:
        #             if char == ')':
        #                 if s[-1] == '(':
        #                     s.pop()
        #                 else:
        #                     return False
        #             elif char == '}':
        #                 if s[-1] == '{':
        #                     s.pop()
        #                 else:
        #                     return False
        #             elif char == ']':
        #                 if s[-1] == '[':
        #                     s.pop()
        #                 else:
        #                     return False
        # return not s
        