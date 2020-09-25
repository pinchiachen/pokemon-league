## 2020/09/25

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        post = head.next
        while post:
            while post and post.val != cur.val:
                post = post.next
                cur = cur.next
                pre = pre.next
            while post and post.val == cur.val:
                post = post.next
            if cur.next != post:
                pre.next = post
                cur = post
                if post:
                    post = post.next
        return dummy.next