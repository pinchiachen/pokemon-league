## 2020/07/14

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1: return []
        return self.dfs(1, n)

    def dfs(self, left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right + 1):
            left_nodes = self.dfs(left, i - 1)
            right_nodes = self.dfs(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res