class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_map = {}
        for n in nums:
            if n in count_map:
                count_map[n]+=1
            else:
                count_map[n] = 1
        min_heap = []
        for n, count in count_map.items():
            heappush(min_heap, (count, n))
            if len(min_heap) > k:
                heappop(min_heap)
        
        result = [n for (count, n) in min_heap]

        return result






















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
        while max_heap:
            _ , num = heapq.heappop(max_heap)
            result.append(num)
        return result[:k]
        