# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        best = [0]  # use list for mutability in nested function
    
        def height(node):
            # If node is None, its height (max edges down to leaf) is -1
            # Using -1 ensures a leaf's height becomes 0: 1 + max(-1, -1) = 0
            if node is None:
                return -1
            
            # Recursively compute left height
            left_h = height(node.left)
            # Recursively compute right height
            right_h = height(node.right)
            
            # Candidate diameter passing through this node equals left_h + right_h + 2 edges
            # That simplifies to (left_h + right_h + 2) = (left_h + 1) + (right_h + 1)
            candidate = left_h + right_h + 2
            
            # Update global best diameter if this candidate is larger
            if candidate > best[0]:
                best[0] = candidate
            
            # Return this node's height to its parent: 1 edge + max of children's heights
            return 1 + (left_h if left_h >= right_h else right_h)
        
        # Kick off the post-order traversal
        height(root)
        
        # After traversal, best[0] holds the maximum number of edges on any path
        return best[0]













        self.max_diameter = 0

        def compute_depth(node):
            if not node:
                return 0
            left_depth = compute_depth(node.left)
            right_depth = compute_depth(node.right)
            self.max_diameter = max(self.max_diameter, left_depth+right_depth)
            return 1+max(left_depth, right_depth)

        compute_depth(root)
        return self.max_diameter

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.max_diameter = 0
        self.compute_depth(root)
        return self.max_diameter
    
    def compute_depth(self, root):
        if root is None:
            return 0
        else:
            left_depth = self.compute_depth(root.left)
            right_depth = self.compute_depth(root.right)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)