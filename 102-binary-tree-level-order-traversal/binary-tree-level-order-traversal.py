# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """


        result = []
        if not root:
            return result
        q = [root]
        while q:
            level = []
            q_len = len(q)
            while q_len:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
                q_len-=1
            result.append(level)
        return result




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        arr = []
        if root is None:
            return arr
        q = [root]
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(level)
        return arr
        