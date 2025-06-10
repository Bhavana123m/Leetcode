# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        view = []
        if not root:
            return view
        
        q = [root]

        while q:
            q_len = len(q)
            while q_len:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if q_len == 1:
                    view.append(node.val)
                q_len -=1
        return view
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        q = [root]
        arr = []
        if root is None:
            return arr
        while q:
            level =[]
            for i in range(len(q)):
                node = q.pop(0)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                level.append(node.val)
            arr.append(level.pop(0))
        return arr
        