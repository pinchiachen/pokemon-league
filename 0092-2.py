## 2021/06/05

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        cur = head
        pre = None
        i = 1
        while i < m:
            pre = cur
            cur = cur.next
            i += 1
        tail_of_first_part = pre
        tail_of_sub_list = cur
        next = None
        i = 0
        while cur and i < n - m + 1:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            i += 1
        if tail_of_first_part:
            tail_of_first_part.next = pre
        else:
            head = pre
        tail_of_sub_list.next = cur
        return head