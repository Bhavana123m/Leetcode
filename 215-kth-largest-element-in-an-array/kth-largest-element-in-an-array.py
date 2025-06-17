class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
                continue
            elif n > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, n)
        return min_heap[0]