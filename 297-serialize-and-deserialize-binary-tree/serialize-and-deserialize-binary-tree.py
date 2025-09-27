# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/7217651/easy-python-bfs-solution-binary-tree-o-n-time-o-n-space-passes-all-cases
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'null':
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i =1 
        while q:
            node = q.popleft()
            # Process left child
            if i < len(nodes) and nodes[i]!='null':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i+=1
             # Process right child  
            if i < len(nodes) and nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))