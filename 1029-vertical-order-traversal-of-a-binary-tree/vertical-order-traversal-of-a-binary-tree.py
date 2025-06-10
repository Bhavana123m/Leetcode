# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import OrderedDict

    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        def sort_by_y_val(pair):
            return (pair[0], pair[1])
        
        coord_val = defaultdict(list)
        result = []
        if not root:
            return result
        self.preorder(coord_val, root, 0, 0)
        for x in sorted(coord_val.keys()): 
            level = sorted(coord_val[x], key=sort_by_y_val)
            result.append([val for y, val in level])
        return result
         
    def preorder(self, coord_val, root, x, y):
        if not root:
            return 
        coord_val[x].append((y, root.val))
        self.preorder(coord_val, root.left, x-1, y+1)
        self.preorder(coord_val, root.right, x+1, y+1)