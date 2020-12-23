## 2020/12/23

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = self.traversal(root, [], k)
        return arr[k-1]

    def traversal(self, root, arr, k):
        if not root or len(arr) >= k: return
        self.traversal(root.left, arr, k)
        arr.append(root.val)
        self.traversal(root.right, arr, k)
        return arr