# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        index = 0
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(min_heap,(node.val, node))
                # index+=1
        result = ListNode(0)
        current = result
        while min_heap:
            val,node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap,(node.next.val, node.next))
                # index+=1
        return result.next