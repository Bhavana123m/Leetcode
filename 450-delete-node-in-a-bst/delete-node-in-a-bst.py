# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        def dfs(node, key):
            if not node:
                return None
            if key < node.val:
                # Recurse into left subtree and reattach
                node.left = dfs(node.left, key)
                return node
                
            elif key > node.val:
                # Recurse into right subtree and reattach
                node.right = dfs(node.right, key)
                return node
            else:
                # Found the node to delete
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left     
                # to handle what to be replaced there
                # Two children: replace with inorder successor (min of right subtree)
                succ = node.right
                while succ.left:
                    succ = succ.left
                # Copy successor's value into current node
                node.val = succ.val
                # Delete the successor node from the right subtree
                node.right = dfs(node.right, succ.val)
                return node
        
        return dfs(root, key)
        

        