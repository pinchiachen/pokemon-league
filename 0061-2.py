## 2021/06/05

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head
        last = head
        l = 1
        while last.next:
            last = last.next
            l += 1
        last.next = head
        rotate = l - k % l
        tail = None
        while rotate > 0:
            if rotate == 1:
                tail = head
            head = head.next
            rotate -= 1
        tail.next = None
        return head