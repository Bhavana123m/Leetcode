class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num]+=1
            else:
                count_map[num] = 1
        max_heap = []
        result = []
        for n, count in count_map.items():
            heapq.heappush(max_heap, (-count, n))  # count no.of elements in count and use maxheap by using count value
                                                   # and till k = 0 append n to result and give result
        while max_heap:
            _ , num = heapq.heappop(max_heap)
            result.append(num)
        print(result)
        return result[:k]
        