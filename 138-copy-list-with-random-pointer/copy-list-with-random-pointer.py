"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        
        curr = head
        while curr:
            next = curr.next
            curr.next = Node(curr.val, next, None)
            curr = next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        result = head.next
        while curr:
            next = curr.next.next
            copy = curr.next
            curr.next = next
            if next:
                copy.next = next.next
            curr = next
        
        return result