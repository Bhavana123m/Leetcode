class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0]*n
        stack = []
        for i in range(len(logs)):
            details = logs[i].split(':')
            id = int(details[0])
            op = details[1]
            time = int(details[2])
            if op == 'start':
                stack.append([id, time])
            else:
                popped = stack.pop()
                res[popped[0]] += time-popped[1]+1
                if stack:
                    res[stack[-1][0]] -= time-popped[1]+1

        return res



        res = [0]*n
        stack = []
        for i in range(len(logs)):
            details = logs[i].split(':')
            id = int(details[0])
            op = details[1]
            time = int(details[2])
            if op == 'start':
                if stack:
                    res[stack[-1][0]] += time-stack[-1][1]
                stack.append([id, time])
            else:
                popped = stack.pop()
                res[popped[0]] += time-popped[1]+1
                if stack:
                    stack[-1][1] = time+1

        return res