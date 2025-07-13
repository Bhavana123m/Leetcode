# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None   
        prev = None
        curr = head
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        return prev


        # prev = None
        # curr = head
        # # nextp = curr.next
        # while curr:
        #     nextp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextp
        # return prev






        dummy = ListNode(0)
        dummy.next = head
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        curr = dummy
        while stack:
            popped = stack.pop()
            curr.next = popped
            curr = curr.next
        curr.next = None
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        prev = None 
        curr = head
        while curr: 
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode 
        
        return prev