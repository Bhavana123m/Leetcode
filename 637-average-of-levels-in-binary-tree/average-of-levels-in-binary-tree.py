# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        queue = [root]
        res = []
        
        while(queue):
            qlen = len(queue)
            tmp = 0
            for i in range(qlen): 
                node = queue.pop(0)
                tmp += node.val
                if node.left:   
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(float(tmp)/qlen)
        
        return res