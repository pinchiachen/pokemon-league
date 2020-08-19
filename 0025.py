## 2020/08/19

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = head
        count = 1
        while end:
            if count % k == 0:
                start = self.reverseMiddle(start, end.next)
                end = start.next
            else:
                end = end.next
            count += 1
        return dummy.next
    
    def reverseMiddle(self, start, end):
        pre = None
        last = start.next
        head = start.next
        while head != end:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        start.next = pre
        last.next = end
        return last