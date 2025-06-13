import heapq
class MedianFinder(object):

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (float(-self.maxHeap[0] + self.minHeap[0])) /2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()