class MinStack(object):

    def __init__(self):
        self.arr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.arr:
            self.arr.append((val, val))
        else:
            cur_min = self.arr[-1][1]
            self.arr.append((val, min(val, cur_min)))

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.arr[-1][1]
