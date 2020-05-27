# 2020/05/22
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if not node: continue
            res.append(node.val)
            stack.append(root.right)
            stack.append(root.left)
        return res