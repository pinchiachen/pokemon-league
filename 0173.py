## 2020/10/17

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.values = []
        self.__buildArray(root)
        self.length = len(self.values)
        self.index = 0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.values[self.index - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < self.length
    
    def __buildArray(self, root):
        if not root: return
        self.__buildArray(root.left)
        self.values.append(root.val)
        self.__buildArray(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()