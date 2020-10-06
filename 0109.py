## 2020/10/06

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        node_arr = []
        while head:
            node_arr.append(head.val)
            head = head.next
        return self.buildTree(node_arr)

    def buildTree(self, arr):
        if not arr: return None
        index = len(arr) // 2
        root = TreeNode(arr[index])
        root.left = self.buildTree(arr[:index])
        root.right = self.buildTree(arr[index+1:])
        return root
