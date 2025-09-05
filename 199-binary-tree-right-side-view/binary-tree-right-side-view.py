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
        if not root:
            return []
        right_view = []
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)
            while q_len:
                node = q.popleft()
                if q_len == 1:
                    right_view.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                q_len-=1
        return right_view


























        #top down perspective of the tree, as seen from "left to right"
        #Get left view and right view of the tree and append the reveresed left view with the right_view[1:]
        view = []
        if not root:
            return view
        left_view = []
        right_view = []
        q = [root]
        while q:
            q_len = len(q)
            level_len = q_len
            while q_len:
                node = q.pop(0)
                if q_len == 1:
                    left_view.append(node.val)
                elif q_len == level_len:
                    right_view.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                q_len-=1
        # view = reversed(left_view)
        left_view.reverse()
        left_view.extend(right_view)
        # left_
        # for i in right_view:
        #     view.append(i)
        return left_view

        
        
        
        #left view of the tree
        view = []
        if not root:
            return view
        q = [root]
        while q:
            q_len = len(q)
            level_len = q_len
            while q_len:
                node = q.pop(0)
                if level_len == q_len:
                    view.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                q_len-=1
        return view
                
       
       # right side of the tree       
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
        