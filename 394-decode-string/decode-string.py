class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        str_stack = []
        current_str = ""
        current_num = 0

        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            elif c == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num = 0
                current_str = ""
            elif c == ']':
                repeat_times = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * repeat_times
            else:
                current_str += c

        return current_str