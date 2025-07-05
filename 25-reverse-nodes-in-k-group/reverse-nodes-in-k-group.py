# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        stack = []
        curr = head
        dummy = ListNode(0)
        tail = dummy

        while curr:
            while curr and len(stack) <k:
                stack.append(curr)
                curr = curr.next
            if len(stack) == k:
                while stack:
                    node = stack.pop()
                    tail.next = node
                    tail = tail.next
                tail.next = curr
        return dummy.next
            