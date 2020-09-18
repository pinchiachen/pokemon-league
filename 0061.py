## 2020/09/18

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head: return head
        length = 0
        tmp_head = head
        while tmp_head:
            length += 1
            tmp_head = tmp_head.next
        index = k % length
        if index == 0: return head
        fast = head
        low = head
        end = low
        while index > 0:
            fast = fast.next
            index -= 1
        while fast.next:
            fast = fast.next
            low = low.next
        start = low.next
        res = start
        low.next = None
        while start.next:
            start = start.next
        start.next = end
        return res