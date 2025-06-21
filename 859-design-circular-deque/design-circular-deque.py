class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.q = [0]*k
        self.size = 0
        self.head = 0
        self.tail = 0


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.k)%self.k
        self.q[self.head] = value
        self.size+=1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1)%self.k
        self.size+=1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head+1)%self.k
        self.size -=1
        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1 + self.k) % self.k
        self.size -=1
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.head]
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[(self.tail - 1 + self.k) % self.k]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        return False
        
    def isFull(self):
        """
        :rtype: bool
        """
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()