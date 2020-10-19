## 2020/10/19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        post = head.next
        cur = head
        while post:
            while post and post.val != val:
                post = post.next
                cur = cur.next
            while post and post.val == val:
                post = post.next
            if cur.next != post:
                cur.next = post
        return dummy.next