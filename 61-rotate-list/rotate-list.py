# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or k == 0:
            return head
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        k = k % length
        if k == 0:
            return head
        prev = None
        curr = head
        steps = length - k
        while steps > 0:
            prev = curr
            curr = curr.next
            steps -= 1
        new_head = curr
        prev.next = None
        
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head

        return new_head
        # if not head or not head.next or k == 0:
        #     return head
        # length = 1
        # curr = head
        # while curr.next:
        #     curr = curr.next
        #     length+=1
        # k = k % length
        # if k == 0:
        #     return head
        # curr.next = head
        # steps_to_new_tail = length - k
        # new_tail = head
        # count = 1
        # while count < steps_to_new_tail:
        #     new_tail = new_tail.next
        #     count += 1
        # new_head = new_tail.next
        # new_tail.next = None

        # return new_head
            
        