# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        tail = None
        carry = 0

        while l1 or l2 or carry!=0:
            if l1:
                digit1 = l1.val
                l1 = l1.next
            else: digit1 = 0
            if l2:
                digit2 = l2.val
                l2 = l2.next
            else: digit2 = 0
            total = digit1 + digit2 + carry
            carry = total//10
            newNode = ListNode(total%10)
            if not result:
                result = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = tail.next
        return result




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # head = None # result
        # tail = None # pointer to last node of result
        # carry = 0
        # while l1 or l2 or carry!=0:
        #     digit1 = l1.val if l1 else 0
        #     digit2 = l2.val if l2 else 0
        #     sum = digit1 + digit2 + carry
        #     carry = sum / 10
        #     new = ListNode(sum % 10)
        #     if not head:
        #         head = new
        #         tail = new
        #     else:
        #         tail.next = new
        #         tail = tail.next    
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        # return head



        
        