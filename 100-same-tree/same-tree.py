# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False

        # q1 = [p]
        # q2 = [q]
        # while q1 and q2:
        #     node1 = q1.pop(0)
        #     node2 = q2.pop(0)

        #     if not node1 and not node2:
        #         continue
        #     if not node1 or not node2:
        #         return False
        #     if node1.val != node2.val:
        #         return False

        #     q1.append(node1.left)
        #     q2.append(node2.left)
        #     q1.append(node1.right)
        #     q2.append(node2.right)

        # return not q1 and not q2
                