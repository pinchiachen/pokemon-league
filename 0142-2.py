## 2021/05/14

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        visited = {}
        while head:
            if head in visited:
                return head
            else:
                visited[head] = True
                head = head.next
        return None