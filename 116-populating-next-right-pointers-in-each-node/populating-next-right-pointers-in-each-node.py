"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        leftmost = root
        # Since it's a perfect binary tree, if leftmost has a left child,
        # the level below is fully present.
        while leftmost.left:
            cur = leftmost
            while cur:
                # 1) Connect within the same parent
                cur.left.next = cur.right
                # 2) Connect across parents using current level's next
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            # Go down one level
            leftmost = leftmost.left

        return root


        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if i < q_len - 1:
                    node.next = q[0]
                else:
                    node.next = None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root