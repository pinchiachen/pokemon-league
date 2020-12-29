## 2020/12/29

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        self.__traversal(root, nodes)
        return ' '.join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(' ')
        return self.__build(nodes)
    
    def __traversal(self, root, nodes):
        if not root:
            nodes.append('*')
        else:
            nodes.append(str(root.val))
            self.__traversal(root.left, nodes)
            self.__traversal(root.right, nodes)

    def __build(self, nodes):
        if not nodes: return
        val = nodes.pop(0)
        if val == '*': return None
        root = TreeNode(int(val))
        root.left = self.__build(nodes)
        root.right = self.__build(nodes)
        return root