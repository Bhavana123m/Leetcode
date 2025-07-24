class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
                else:
                    continue
            elif log == './':
                continue
            else:
                stack.append(log)
        # print(stack)
        return len(stack)