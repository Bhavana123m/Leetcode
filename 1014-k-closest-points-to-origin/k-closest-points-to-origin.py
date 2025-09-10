class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for i in range(len(points)):
            p = points[i]
            distance = -((p[0]*p[0]) + (p[1]*p[1]))
            if len(heap)<k:
                heapq.heappush(heap, (distance, i))
            else:
                if heap[0][0] < distance:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (distance, i))
        result = []
        for i in heap:
            result.append(points[i[1]])
        return result