## 2020/10/14

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        nodes = []
        count = 1
        while head:
            nodes.append(head)
            head = head.next
        l = len(nodes)
        while count <= l:
            if count % 2 != 0:
                nodes[count//2].next = None if count//2 == l-(count+1)//2 else nodes[l-(count+1)//2]
            else:
                nodes[l-count//2].next = None if l-count//2 == (count+1)//2 else nodes[(count+1)//2]
            count += 1