# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        right = head
        for _ in range(k-1):
            right = right.next
        swap_node = right
        left = head
        while right.next:
            left = left.next
            right = right.next
        left.val, swap_node.val = swap_node.val, left.val
        return head
        # dummyNode = ListNode(0)
        # length = 0
        # curr = head
        # while curr:
        #     length+=1
        #     curr = curr.next
        # first_node_pointer = k
        # second_node_pointer = length-k+1
        # count = 0
        # first_node = None
        # second_node = None
        # curr = head
        # while curr:
        #     count+=1
        #     if count == first_node_pointer:
        #         first_node = curr
        #     if count == second_node_pointer:
        #         second_node = curr
        #     curr = curr.next
        # if first_node and second_node:
        #     first_node.val, second_node.val = second_node.val, first_node.val

        # return head