# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        self.stack = []

        
    def next(self):
        """
        :rtype: int
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        node = self.stack.pop()
        self.root = node.right
        return node.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0 or self.root != None

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()