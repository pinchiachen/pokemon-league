## 2020/10/23

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.nodes = []
        self.__traversal(root)
        return ' '.join(self.nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.vals = data.split(' ')
        return self.__build()

    def __traversal(self, root):
        if not root:
            self.nodes.append('#')
            return
        else:
            self.nodes.append(str(root.val))
        self.__traversal(root.left)
        self.__traversal(root.right)

    def __build(self):
        if not self.vals: return
        cur_val = self.vals.pop(0)
        if cur_val == '#': return None
        root = TreeNode(cur_val)
        root.left = self.__build()
        root.right = self.__build()
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))