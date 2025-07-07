# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        # def builiterator(arr, node, stack):
        #     if not node: 
        #         return
        #     while node.left:
        #         stack.append(node)
        #         node = node.left
            

            
            

        # stack = []
        # arr = []
        # st = builditerator(arr, root, stack)

        def inorder_traversal(node, arr):
            if not node:
                return
            
            inorder_traversal(node.left, arr)
            arr.append(node.val)
            inorder_traversal(node.right, arr)

        arr = []
        inorder_traversal(root, arr) # Populate the array with sorted BST values

        # Two-pointer approach on the sorted array
        left = 0
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else: # current_sum > k
                right -= 1
        
        return False








        seen = set()
        return self.find_seen(root, seen, k)

    def find_seen(self, node, seen, target):
        if not node:
            return False
        if (target - node.val) in seen:
            return True
        seen.add(node.val)
        return self.find_seen(node.left, seen, target) or self.find_seen(node.right, seen, target)
