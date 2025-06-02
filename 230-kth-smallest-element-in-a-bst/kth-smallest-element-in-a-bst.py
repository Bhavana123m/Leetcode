# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Space Complexity - O(1) for sorted_arr and Time Complexity - O(n)
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count = 0
        value = -1
        self.inOrder(root, count, value, k)
        return value
    
    def inOrder(self, root, count, value, k):
        if not root:
            return
        self.inOrder(root.left, count, value, k)
        count+=1
        if count == k:
            value = root.val
            return
        self.inOrder(root.right, count, value, k)

    # Space Complexity - O(n) for sorted_arr and Time Complexity - O(n)
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        sorted_arr = []
        self.inOrder(root, sorted_arr)
        return sorted_arr[k-1]
    
    def inOrder(self, root, arr):
        if not root:
            return
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)