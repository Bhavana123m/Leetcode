# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        q = [root]
        height = 0
        count = 0
        left_to_right = True
        while q:
            level = []
            count +=1
            q_len = len(q)
            while q_len:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
                q_len-=1
            
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right

        return result