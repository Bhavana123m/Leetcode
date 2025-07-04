# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        if not list1 and not list2:
            return None
        if list1 and list2:
            heapq.heappush(min_heap,(list1.val, list1))
            heapq.heappush(min_heap,(list2.val, list2))
        elif list1 and not list2:
            heapq.heappush(min_heap,(list1.val, list1))
        elif not list1 and list2:
            heapq.heappush(min_heap,(list2.val, list2))
        result = ListNode(0)
        curr = result
        while min_heap:
            val, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap,(node.next.val, node.next))
        return result.next
            
        
        