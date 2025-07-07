class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = {}
        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task]+=1
        max_heap = []
        for c in count.values():
            max_heap.append(-c)
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            time +=1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append((cnt, time+n))
            if q and time == q[0][1]:
                heapq.heappush(max_heap, q.popleft()[0])
        return time

