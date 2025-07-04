# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        n = len(stack)
        curr = head
        for _ in range(n//2):
            pop_address = stack.pop()
            curr_next = curr.next
            curr.next = pop_address
            pop_address.next = curr_next
            curr = curr_next
        curr.next = None
        return head

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        mid = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
        list2 = mid.next
        mid.next = None
        p1 = list2
        back = None
        while p1:
            temp = p1.next
            p1.next = back
            back = p1
            p1 = temp
        p2 = head
        while back and p2:
            temp2 = p2.next
            tempB = back.next
            p2.next = back
            back.next = temp2
            back = tempB
            p2 = temp2
        return head
        # fast = head
        # slow = head
        # while slow and fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # prev = None
        # curr = slow.next
        # slow.next = None
        # while curr:
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
        # first = head
        # second = prev
        # while second:
        #     tmp1 = first.next
        #     tmp2 = second.next

        #     first.next = second
        #     second.next = tmp1

        #     first = tmp1
        #     second = tmp2