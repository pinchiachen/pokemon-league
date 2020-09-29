## 2020/09/29

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return head
        cur = ListNode(0)
        cur.next = head
        dummy = cur
        post = head
        pos = 1
        while post:
            while post and pos != m:
                post = post.next
                cur = cur.next
                pos += 1
            if pos == m:
                count = 0
                current = post
                pre = None
                while current and count <= n-m:
                    tmp = current
                    current = current.next
                    tmp.next = pre
                    pre = tmp
                    count += 1
            cur.next = pre
            break
        while cur.next:
            cur = cur.next
        cur.next = current
        return dummy.next